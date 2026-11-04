# #612 Ren'Py

Voce canonica `Ren'Py`, tipo `programming`, language_id `322`.

Show greeting as a dialogue at the start point of an original Ren’Py project.

## Toolchain and reproduction

Required genuine renpy compiler/runtime, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Requires Ren’Py SDK compatible and project in current directory with game/script.rpy.

Comando/procedura from the directory of the example, unless explicit indications:

```text
renpy . lint; renpy .
```

Expected result: Hello, World! in output or compliant data, according to the scope described.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Source original label start and statement dialog, no comment. SDK/lint/display unconfigured.

Remaining requirements:

- Required renpy compiler/runtime and matching host resources are not available/configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.renpy.org/doc/html/quickstart.html](https://www.renpy.org/doc/html/quickstart.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.rpy` | [script.rpy](game/script.rpy) created; verification pending |
