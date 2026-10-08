"""Find corpus examples and recorded evidence without running a toolchain.

Uses the Python standard library. IDs, states and commands come from the frozen
reference and existing trackers; a recorded success is not a new execution.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path, PurePosixPath
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
COUNT = 836
REFERENCE_SHA256 = "183243e30496ba53f5f8743b0e39c9f0e0bccc5a32639f7b541cc2285db0e043"
INDEX = ROOT / "tracking/agent_index.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def portable_path(relative: str) -> str:
    path = PurePosixPath(relative)
    require(bool(relative) and not path.is_absolute() and ".." not in path.parts
            and ":" not in relative and "\\" not in relative,
            f"Unsafe or nonportable recorded path: {relative}")
    require((ROOT / relative).resolve().is_relative_to(ROOT),
            f"Recorded path escapes the corpus: {relative}")
    return relative


def normalized(value: str) -> str:
    # Windows folder names use U+2217 for the two canonical names containing *.
    return unicodedata.normalize("NFKC", value).replace("∗", "*").casefold()


def load_sources() -> tuple[list[dict], dict[int, list[dict]]]:
    require(digest(ROOT / "reference/languages.yml") == REFERENCE_SHA256,
            "Canonical languages.yml changed; do not rebuild IDs from another snapshot")
    tracker = read_json("tracking/languages_tracker.json")
    baseline = read_json("tracking/extensions_baseline.json")
    extension_tracker = read_json("tracking/extensions_tracker.json")
    entries = tracker["entries"]
    require(tracker["language_count"] == COUNT and len(entries) == COUNT,
            "Expected 836 canonical entries")
    require(baseline["reference_sha256"] == REFERENCE_SHA256
            and extension_tracker["reference_sha256"] == REFERENCE_SHA256,
            "Extension metadata belongs to a different reference")
    with (ROOT / "reference/languages.csv").open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    require(len(rows) == COUNT and len(baseline["entries"]) == COUNT,
            "Reference metadata count mismatch")
    require(len({entry["linguist"]["language_id"] for entry in entries}) == COUNT,
            "Duplicate upstream language_id")
    expected_pairs = set()
    for ordinal, (entry, row, ext) in enumerate(zip(entries, rows, baseline["entries"]), 1):
        require(entry["ordinal"] == ext["ordinal"] == int(row["ordinal"]) == ordinal,
                f"Canonical ordinal mismatch at #{ordinal:03d}")
        require(entry["name"] == row["name"] == ext["name"],
                f"Canonical name mismatch at #{ordinal:03d}")
        require(entry["linguist"]["language_id"] == int(row["language_id"]),
                f"Upstream ID mismatch at #{ordinal:03d}")
        require(entry["linguist"]["extensions"] == ext["extensions"],
                f"Canonical extensions mismatch at #{ordinal:03d}")
        portable_path(entry["folder"])
        expected_pairs.update((ordinal, suffix) for suffix in ext["extensions"])
    variants: dict[int, list[dict]] = {entry["ordinal"]: [] for entry in entries}
    seen_pairs = set()
    for variant in extension_tracker["entries"]:
        ordinal = variant["language_ordinal"]
        pair = (ordinal, variant["extension"])
        require(pair in expected_pairs and pair not in seen_pairs,
                f"Unknown or duplicate language/extension pair: {pair}")
        require(variant["language_name"] == entries[ordinal - 1]["name"],
                f"Extension name mismatch at #{ordinal:03d}")
        seen_pairs.add(pair)
        variants[ordinal].append(variant)
    require(seen_pairs == expected_pairs, "Extension tracker is incomplete")
    return entries, variants


def summary(entries: list[dict]) -> dict:
    states = [entry["tracking"] for entry in entries]
    return {
        "total": len(entries),
        "artifact_created": sum(state["artifact_created"] for state in states),
        "syntax_verified": sum(state["syntax_verified"] for state in states),
        "semantic_verified": sum(state["semantic_verified"] for state in states),
        "blocked": sum(bool(state["blockers"]) for state in states),
        "verification_basis": "Recorded tracker evidence, not a new execution",
    }


def make_index(entries: list[dict], variants: dict[int, list[dict]]) -> dict:
    result = []
    for entry in entries:
        metadata, state = entry["linguist"], entry["tracking"]
        extensions = variants[entry["ordinal"]]
        result.append({
            "ordinal": entry["ordinal"], "name": entry["name"],
            "language_id": metadata["language_id"], "type": metadata["type"],
            "group": metadata["group"], "aliases": metadata["aliases"],
            "extensions": metadata["extensions"], "filenames": metadata["filenames"],
            "interpreters": metadata["interpreters"],
            "folder": entry["folder"], "readme": entry["folder"] + "/README.md",
            "implementation_status": state["implementation_status"],
            "existence_verified": state["existence_verified"],
            "artifact_created": state["artifact_created"],
            "syntax_verified": state["syntax_verified"],
            "semantic_verified": state["semantic_verified"],
            "verification_status": state["verification_status"],
            "blocker_count": len(state["blockers"]),
            "declared_file_count": len(entry["example"]["files"]),
            "extension_pairs_with_artifacts": sum(v["artifact_created"] for v in extensions),
            "missing_extensions": [v["extension"] for v in extensions if not v["artifact_created"]],
        })
    return {
        "schema_version": 1, "canonical_reference_sha256": REFERENCE_SHA256,
        "source_files_sha256": {
            path: digest(ROOT / path) for path in (
                "tracking/languages_tracker.json", "tracking/extensions_tracker.json",
                "tracking/extensions_baseline.json", "reference/languages.csv")
        },
        "summary": summary(entries), "entries": result,
    }


def detailed_record(entry: dict, variants: list[dict]) -> dict:
    example, state = entry["example"], entry["tracking"]
    for path in example["files"]:
        portable_path(path)
    if state["verification_log"]:
        portable_path(state["verification_log"])
    return {
        "ordinal": entry["ordinal"], "name": entry["name"],
        "linguist": entry["linguist"], "folder": entry["folder"],
        "readme": entry["folder"] + "/README.md", "example": example,
        "tracking": state, "extension_variants": variants,
    }


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("query", nargs="?", help="Exact name/alias, #ordinal, or extension starting with .")
    selector = result.add_mutually_exclusive_group()
    selector.add_argument("--ordinal", type=int, help="Stable corpus number, 1 to 836")
    selector.add_argument("--language-id", type=int, help="Upstream Linguist ID, distinct from corpus number")
    selector.add_argument("--name", help="Exact canonical name or alias, ignoring case")
    selector.add_argument("--contains", help="Substring of canonical name or alias")
    selector.add_argument("--extension", help="Canonical extension; shared suffixes return all matches")
    selector.add_argument("--filename", help="Canonical special filename such as Makefile")
    result.add_argument("--type", choices=("programming", "markup", "data", "prose"))
    result.add_argument("--status", choices=("pending", "blocked", "syntax-verified", "semantic-verified", "unverified"))
    result.add_argument("--json", action="store_true", help="Structured UTF-8 JSON")
    operation = result.add_mutually_exclusive_group()
    operation.add_argument("--write-index", action="store_true", help="Refresh derived tracking/agent_index.json")
    operation.add_argument("--check-index", action="store_true", help="Check the derived index without writing")
    return result


def main() -> int:
    cli = parser()
    args = cli.parse_args()
    selector_fields = ("ordinal", "language_id", "name", "contains", "extension", "filename")
    if args.query:
        if any(getattr(args, key) is not None for key in selector_fields):
            cli.error("Use either a positional query or an explicit selector")
        if args.query.startswith("#"):
            try:
                args.ordinal = int(args.query[1:])
            except ValueError:
                cli.error("A corpus number must look like #014")
        elif args.query.startswith("."):
            args.extension = args.query
        else:
            args.name = args.query
    has_filter = any(getattr(args, key) is not None for key in selector_fields) or args.type or args.status
    if (args.write_index or args.check_index) and has_filter:
        cli.error("Index operations do not accept lookup filters")
    if args.ordinal is not None and not 1 <= args.ordinal <= COUNT:
        cli.error("Corpus ordinal must be between 1 and 836")
    if args.language_id is not None and args.language_id < 0:
        cli.error("language_id must be nonnegative; 0 is valid")
    entries, variants = load_sources()
    if args.write_index or args.check_index:
        expected = make_index(entries, variants)
        if args.write_index:
            INDEX.write_text(json.dumps(expected, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        else:
            require(read_json("tracking/agent_index.json") == expected,
                    "Agent index is stale; run python tools/query_corpus.py --write-index")
        print("OK: agent index binds 836 canonical entries to the current source metadata")
        return 0
    if not has_filter:
        print(json.dumps({"reference_sha256": REFERENCE_SHA256, **summary(entries)}, ensure_ascii=False, indent=2))
        return 0
    matches = []
    for entry in entries:
        metadata, state = entry["linguist"], entry["tracking"]
        names = [entry["name"], *metadata["aliases"]]
        if args.ordinal is not None and entry["ordinal"] != args.ordinal:
            continue
        if args.language_id is not None and metadata["language_id"] != args.language_id:
            continue
        if args.name is not None and normalized(args.name) not in map(normalized, names):
            continue
        if args.contains is not None and not any(normalized(args.contains) in normalized(name) for name in names):
            continue
        if args.extension is not None and normalized(args.extension) not in map(normalized, metadata["extensions"]):
            continue
        if args.filename is not None and normalized(args.filename) not in map(normalized, metadata["filenames"]):
            continue
        if args.type is not None and metadata["type"] != args.type:
            continue
        if args.status == "pending" and state["syntax_verified"] and state["semantic_verified"]:
            continue
        if args.status == "blocked" and not state["blockers"]:
            continue
        if args.status == "syntax-verified" and not state["syntax_verified"]:
            continue
        if args.status == "semantic-verified" and not state["semantic_verified"]:
            continue
        if args.status == "unverified" and (state["syntax_verified"] or state["semantic_verified"]):
            continue
        matches.append(detailed_record(entry, variants[entry["ordinal"]]))
    if args.json:
        print(json.dumps({"reference_sha256": REFERENCE_SHA256, "match_count": len(matches), "entries": matches},
                         ensure_ascii=False, indent=2))
    elif not matches:
        print("No matching canonical entries")
    else:
        for entry in matches:
            state, example = entry["tracking"], entry["example"]
            print(f"#{entry['ordinal']:03d} {entry['name']} (language_id {entry['linguist']['language_id']})")
            print(f"  Type: {entry['linguist']['type']}; group: {entry['linguist']['group'] or entry['name']}")
            print(f"  Recorded: syntax={state['syntax_verified']}, semantics={state['semantic_verified']}, status={state['verification_status']}")
            print(f"  README: {entry['readme']}")
            for path in example["files"]:
                print(f"  File: {path}")
            print(f"  Toolchain: {example['toolchain']}")
            if example["build_command"]:
                print(f"  Build: {example['build_command']}")
            print(f"  Run/check: {example['run_or_check_command']}")
            print(f"  Expected: {example['expected_result']}")
            if state["verification_log"]:
                print(f"  Evidence: {state['verification_log']}")
            for blocker in state["blockers"]:
                print(f"  Blocker: {blocker}")
    return 0 if matches else 1


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    try:
        raise SystemExit(main())
    except (ValueError, KeyError, OSError) as error:
        raise SystemExit(f"QUERY FAILED: {error}")
