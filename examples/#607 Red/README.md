# #607 Red

Voce canonica `Red`, tipo `programming`, language_id `320`.

Run a Red program with compote string and print.

## Toolchain and reproduction

Required genuine red compiler/runtime, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Requires official Red distribution with console/runtime compatible.

Comando/procedura from the directory of the example, unless explicit indications:

```text
red hello.red
```

Expected result: Hello, World! in output or compliant data, according to the scope described.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Sorgente Red originale; toolchain non configurata. Red e Rebol sono verificati separatamente.

Remaining requirements:

- Required red compiler/runtime and matching host resources are not available/configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.red-lang.org/p/documentation.html](https://www.red-lang.org/p/documentation.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.red` | [hello.red](hello.red) created; verification pending |
| `.reds` | [hello.reds](variants/reds-e7c6c4d7/hello.reds) created; verification pending |
