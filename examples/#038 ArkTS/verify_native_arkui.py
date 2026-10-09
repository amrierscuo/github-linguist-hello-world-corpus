"""Prepare/run a task-local native ArkUI compiler harness, never ordinary tsc.

Based on OpenHarmony-5.0.0-Release compiler/main.js and webpack.config.js.
This is a page compilation harness, not a full HAP application. It deliberately
does not mark tracker success or claim native rendering. Use --compile only after
the official SDK archive has passed the upstream SHA-256 check.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys


def digest(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def json_file(path: pathlib.Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def discover_loader(sdk_root: pathlib.Path) -> pathlib.Path:
    configs = [
        p for p in sdk_root.rglob("webpack.config.js")
        if p.parent.name == "ets-loader" and (p.parent / "main.js").is_file()
    ]
    if len(configs) != 1:
        raise RuntimeError(f"Expected one SDK ets-loader, found {len(configs)}: {configs}")
    return configs[0].parent


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--sdk-root", required=True, type=pathlib.Path)
    ap.add_argument("--source", required=True, type=pathlib.Path)
    ap.add_argument("--node", required=True, type=pathlib.Path)
    ap.add_argument("--project", type=pathlib.Path, required=True, help="External working directory for all generated artifacts")
    ap.add_argument("--compile", action="store_true", help="Run the real SDK ArkUI loader and es2abc")
    args = ap.parse_args()
    sdk_root = args.sdk_root.resolve(strict=True)
    source = args.source.resolve(strict=True)
    node = args.node.resolve(strict=True)
    project = args.project.resolve()
    loader = discover_loader(sdk_root)
    webpack = loader / "node_modules" / "webpack" / "bin" / "webpack.js"
    fork_ts_json = loader / "node_modules" / "typescript" / "package.json"
    es2abc = loader / "bin" / "ark" / "build-win" / "bin" / "es2abc.exe"
    for path in (webpack, fork_ts_json, es2abc):
        if not path.is_file():
            raise RuntimeError(f"Required native SDK component missing: {path}")
    source_hash = digest(source)
    page = project / "entry" / "src" / "main" / "ets" / "pages" / "Index.ets"
    page.parent.mkdir(parents=True, exist_ok=True)
    if page.exists() and digest(page) != source_hash:
        raise RuntimeError("Existing harness Index.ets differs; select a fresh --project instead of overwriting it")
    page.write_bytes(source.read_bytes())
    profile = project / "entry" / "src" / "main" / "resources" / "base" / "profile"
    module_path = project / "module.json"
    build_json = project / "build.json"
    build_path = project / "compiler-output"
    cache_path = project / "compiler-cache"
    # The SDK GenAbcPlugin writes preBuildInfo.json during plugin setup, before
    # Webpack initializes its own cache. A real SDK project creates this directory
    # before launching the compiler; without it the bytecode can still be emitted
    # while a separate asynchronous write reports an ArkTS diagnostic error.
    cache_path.mkdir(parents=True, exist_ok=True)
    json_file(module_path, {
        "app": {"bundleName": "org.corpus.arktshello", "minAPIVersion": 12, "targetAPIVersion": 12},
        "module": {"name": "entry", "type": "entry", "pages": "$profile:main_pages", "abilities": []},
    })
    json_file(profile / "main_pages.json", {"src": ["pages/Index"]})
    json_file(build_json, {
        "compileMode": "jsbundle", "pandaMode": "es2abc", "compileEntry": [],
        "projectRootPath": str(project), "modulePathMap": {"entry": str(project / "entry")},
        "moduleName": "entry", "isOhosTest": False,
    })
    json_file(project / "runtime-resources" / "module.json", json.loads(module_path.read_text(encoding="utf-8")))
    json_file(project / "runtime-resources" / "resources" / "base" / "profile" / "main_pages.json", {"src": ["pages/Index"]})
    # SDK webpack consumes these process environment variables before its --env
    # options are processed. All values apply only to this child process.
    task_env = {
        "aceModuleRoot": str(project / "entry" / "src" / "main" / "ets"),
        "aceModuleBuild": str(build_path),
        "aceModuleJsonPath": str(module_path),
        "aceProfilePath": str(profile),
        "aceBuildJson": str(build_json),
        "cachePath": str(cache_path),
        "minPlatformVersion": "12",
        "abilityType": "page",
        "runtimeOS": "OpenHarmony",
        "watchMode": "false",
    }
    command = [str(node), str(webpack), "--config", str(loader / "webpack.config.js"),
               "--env", "buildMode=debug", "--env", "compilerType=ark", "--env", f"nodeJs={node}"]
    metadata = {
        "prepared_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "source_path": str(source), "source_sha256": source_hash,
        "copied_source_sha256": digest(page), "sdk_loader": str(loader),
        "sdk_typescript_package": json.loads(fork_ts_json.read_text(encoding="utf-8")),
        "node_version": subprocess.run([str(node), "--version"], capture_output=True, text=True).stdout.strip(),
        "command": command, "cwd": str(loader), "environment": task_env,
        "sources": [
            "https://github.com/openharmony/developtools_ace_ets2bundle/blob/OpenHarmony-5.0.0-Release/compiler/main.js",
            "https://github.com/openharmony/developtools_ace_ets2bundle/blob/OpenHarmony-5.0.0-Release/compiler/webpack.config.js",
        ],
        "scope": "Real ArkTS/ArkUI SDK page compilation and ABC generation; not a complete HAP or native rendering proof.",
        "executed": False, "semantic_rendering_verified": False,
    }
    # Do not create a full application license/manifest or install npm replacements.
    # The SDK provides its native compiler fork and its prebuilt dependencies.
    json_file(project / "harness_prepared.json", metadata)
    print(json.dumps({"project": str(project), "loader": str(loader), "node": str(node),
                      "source_sha256": source_hash, "command": command, "will_compile": args.compile}))
    if not args.compile:
        return 0
    env = os.environ.copy()
    env.update(task_env)
    result = subprocess.run(command, cwd=loader, env=env, capture_output=True, text=True,
                            encoding="utf-8", errors="replace", timeout=300)
    (project / "compiler_stdout.txt").write_text(result.stdout, encoding="utf-8")
    (project / "compiler_stderr.txt").write_text(result.stderr, encoding="utf-8")
    metadata.update({
        "executed": True, "finished_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "exit_code": result.returncode,
        "source_sha256_after": digest(source), "copied_source_sha256_after": digest(page),
        "artifacts": [{"path": str(p.relative_to(project)), "size": p.stat().st_size, "sha256": digest(p)}
                      for p in build_path.rglob("*") if p.is_file()],
        "compiler_success_banner": "COMPILE RESULT:SUCCESS" in result.stdout,
        "arkts_error_diagnostics": re.findall(r"ArkTS:ERROR[^\r\n]*", result.stdout + "\n" + result.stderr),
    })
    metadata["page_js_exists"] = (build_path / "pages" / "Index.js").is_file()
    metadata["page_abc_exists"] = (build_path / "pages" / "Index.abc").is_file()
    metadata["native_page_compilation_passed"] = (
        result.returncode == 0 and not metadata["arkts_error_diagnostics"]
        and metadata["page_js_exists"] and metadata["page_abc_exists"]
    )
    json_file(project / "harness_compiled.json", metadata)
    print(result.stdout)
    print(result.stderr, file=sys.stderr)
    if digest(source) != source_hash or digest(page) != source_hash:
        raise RuntimeError("Index.ets changed during native compilation")
    return 0 if metadata["native_page_compilation_passed"] else (result.returncode or 1)


if __name__ == "__main__":
    raise SystemExit(main())
