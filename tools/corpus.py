"""Audit the frozen corpus baseline and refresh counts/checksums (stdlib only)."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
COUNT = 836
REFERENCE_HASH = "183243e30496ba53f5f8743b0e39c9f0e0bccc5a32639f7b541cc2285db0e043"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def inside(relative: str) -> Path:
    require(isinstance(relative, str) and bool(relative), "Empty or invalid path")
    posix = PurePosixPath(relative)
    require(not posix.is_absolute() and ".." not in posix.parts,
            f"Unsafe path: {relative}")
    require("\\" not in relative and ":" not in relative,
            f"Paths must be portable and relative: {relative}")
    path = (ROOT / relative).resolve()
    require(path.is_relative_to(ROOT), f"Path outside corpus: {relative}")
    return path


def load_and_audit() -> dict:
    require(digest(ROOT / "reference/languages.yml") == REFERENCE_HASH,
            "The canonical languages.yml has changed")
    # The seed manifest includes the ORIGINAL tracker/README. Only its frozen
    # reference files should still match after the corpus has been populated.
    for line in (ROOT / "reference/SHA256SUMS.txt").read_text().splitlines():
        expected, relative = line.split("  ", 1)
        if relative.startswith("reference/"):
            require(digest(inside(relative)) == expected,
                    f"Frozen seed reference changed: {relative}")

    tracker = json.loads((ROOT / "tracking/languages_tracker.json").read_text(encoding="utf-8"))
    entries = tracker["entries"]
    require(tracker["language_count"] == COUNT and len(entries) == COUNT,
            "Expected exactly 836 canonical entries")
    with (ROOT / "reference/languages.csv").open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    numbered = [line.split("\t", 1) for line in
                (ROOT / "reference/languages.txt").read_text(encoding="utf-8").splitlines()]
    require(len(rows) == COUNT and len(numbered) == COUNT, "Reference list count mismatch")
    require(len({entry["name"] for entry in entries}) == COUNT, "Duplicate canonical name")
    require(len({entry["linguist"]["language_id"] for entry in entries}) == COUNT,
            "Duplicate canonical language_id")
    require(len({entry["folder"] for entry in entries}) == COUNT, "Duplicate example folder")

    for ordinal, (entry, row, line) in enumerate(zip(entries, rows, numbered), 1):
        label = f"{ordinal:04d} {entry['name']}"
        require(entry["ordinal"] == ordinal == int(row["ordinal"]) == int(line[0]),
                f"Canonical ordinal mismatch: {label}")
        require(entry["name"] == row["name"] == line[1], f"Canonical name mismatch: {label}")
        metadata = entry["linguist"]
        require(metadata["language_id"] == int(row["language_id"]), f"ID mismatch: {label}")
        require(metadata["type"] == row["type"], f"Type mismatch: {label}")
        extensions = metadata["extensions"]
        require((extensions[0] if extensions else "") == row["primary_extension"],
                f"Primary extension mismatch: {label}")
        folder = inside(entry["folder"])
        require(entry["folder"] == f"examples/#{ordinal:03d} " + entry["name"].replace("*", "∗"),
                f"Folder does not preserve canonical order: {label}")
        tracking = entry["tracking"]
        for field in ("artifact_created", "syntax_verified", "semantic_verified"):
            require(isinstance(tracking[field], bool), f"Invalid flag {field}: {label}")
        require(not tracking["semantic_verified"] or tracking["syntax_verified"],
                f"Semantic verification requires syntax verification: {label}")
        require(not tracking["syntax_verified"] or tracking["artifact_created"],
                f"Verification without an artifact: {label}")
        example = entry["example"]
        if tracking["artifact_created"]:
            require(folder.is_dir(), f"Missing example folder: {label}")
            require((folder / "README.md").is_file(), f"Missing example instructions: {label}")
            require(bool(example["files"]), f"No artifact files declared: {label}")
            for relative in example["files"]:
                path = inside(relative)
                require(path.is_relative_to(folder), f"File outside example folder: {relative}")
                require(path.is_file() and path.stat().st_size > 0, f"Missing/empty artifact: {relative}")
            for field in ("semantic_goal", "validation_mode", "toolchain",
                          "run_or_check_command", "expected_result"):
                require(bool(example[field]), f"Missing {field}: {label}")
            require(bool(example.get("sources")), f"Missing primary sources: {label}")
            require(tracking["implementation_status"] != "not_started", f"Created but not started: {label}")
        else:
            require(not example["files"], f"Uncreated artifact declares files: {label}")
        if tracking["syntax_verified"] or tracking["semantic_verified"]:
            require(bool(tracking["verification_timestamp_utc"]), f"No check timestamp: {label}")
            require(bool(tracking["verification_platform"]), f"No check platform: {label}")
            require(bool(tracking["verification_log"]), f"No evidence log: {label}")
            log = inside(tracking["verification_log"])
            require(log.is_file() and log.stat().st_size > 0, f"Missing evidence: {label}")
            verified_hashes = tracking.get("verified_artifact_sha256")
            require(isinstance(verified_hashes, dict) and bool(verified_hashes),
                    f"No artifact hashes bound to the recorded verification: {label}")
            for relative, expected in verified_hashes.items():
                require(relative in example["files"], f"Verified file is not declared: {relative}")
                path = inside(relative)
                require(path.is_file() and digest(path) == expected,
                        f"Previously verified artifact changed; rerun its validator: {relative}")
    return tracker


def progress(tracker: dict) -> dict:
    states = [entry["tracking"] for entry in tracker["entries"]]
    created = sum(state["artifact_created"] for state in states)
    syntax = sum(state["syntax_verified"] for state in states)
    semantic = sum(state["semantic_verified"] for state in states)
    complete = sum(state["syntax_verified"] and state["semantic_verified"] for state in states)
    return {
        "total": COUNT,
        "not_started": COUNT - created,
        "artifact_created": created,
        "syntax_verified": syntax,
        "semantic_verified": semantic,
        "blocked": sum(bool(state["blockers"]) for state in states),
        "completion_percent": round(100 * complete / COUNT, 4),
        "artifact_created_percent": round(100 * created / COUNT, 4),
        "completion_basis": "syntax_verified AND semantic_verified",
    }


def tracked_files() -> list[Path]:
    # Dependency installations/build products are not part of the deliverable.
    excluded = {".git", "__pycache__", "node_modules", ".venv", "build", "dist", ".tools", ".jac", ".jitted_scripts"}
    tracker = json.loads((ROOT / "tracking/languages_tracker.json").read_text(encoding="utf-8"))
    declared = {p for entry in tracker["entries"] for p in entry["example"]["files"]}
    declared.update(entry["tracking"]["verification_log"] for entry in tracker["entries"] if entry["tracking"]["verification_log"])
    files = []
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        required = relative.as_posix() in declared
        if path.is_file() and path != ROOT / "SHA256SUMS.txt" and (required or not (set(relative.parts) & excluded)):
            files.append(path)
    return sorted(files, key=lambda path: path.relative_to(ROOT).as_posix())


def refresh(tracker: dict) -> None:
    (ROOT / "tracking/progress.json").write_text(
        json.dumps(progress(tracker), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    manifest = "".join(f"{digest(path)}  {path.relative_to(ROOT).as_posix()}\n"
                       for path in tracked_files())
    (ROOT / "SHA256SUMS.txt").write_text(manifest, encoding="utf-8")


def check_manifest() -> None:
    manifest = ROOT / "SHA256SUMS.txt"
    require(manifest.is_file(), "Current corpus checksum manifest missing; run refresh")
    listed = []
    for line in manifest.read_text(encoding="utf-8").splitlines():
        expected, relative = line.split("  ", 1)
        path = inside(relative)
        require(path.is_file() and digest(path) == expected, f"Corpus checksum mismatch: {relative}")
        listed.append(relative)
    actual = [path.relative_to(ROOT).as_posix() for path in tracked_files()]
    require(listed == actual, "Checksum manifest does not match corpus files")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("audit", "refresh"))
    args = parser.parse_args()
    tracker = load_and_audit()
    if args.action == "refresh":
        refresh(tracker)
    expected = progress(tracker)
    recorded = json.loads((ROOT / "tracking/progress.json").read_text(encoding="utf-8"))
    require(recorded == expected, "Progress counters are stale; run refresh")
    check_manifest()
    print(f"OK: {COUNT} canonical entries; immutable references, artifact files, evidence, counters and checksums")
    print(json.dumps(expected, ensure_ascii=False, indent=2))
    print("Integrity checks do not compile or run language examples; consult each verification log.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, OSError) as error:
        raise SystemExit(f"AUDIT FAILED: {error}")
