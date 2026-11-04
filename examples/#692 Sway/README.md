# #692 Sway

Voce canonica `Sway`, tipo `programming`, language_id `271471144`.

Return a string of 13 characters from an original Sway script.

## Toolchain and reproduction

Required genuine forc compiler/runtime, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Requires Fuel Sway compiler/forc and a compatible local runner, without sending transactions.

Comando/procedura from the directory of the example, unless explicit indications:

```text
forc build; forc run --dry-run
```

Expected result: Hello, World! in the conformed result, according to the framework described.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Sway indicates the language Fuel, with str[ 13 ]; the program is not a configuration of the window manager of the same name. Toolchain absent.

Remaining requirements:

- Required forc toolchain and matching execution/format resources are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://fuellabs.github.io/sway/v0.31.0/basics/variables.html](https://fuellabs.github.io/sway/v0.31.0/basics/variables.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.sw` | [main.sw](src/main.sw) created; verification pending |
