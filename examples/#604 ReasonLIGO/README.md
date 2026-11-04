# #604 ReasonLIGO

Voce canonica `ReasonLIGO`, tipo `programming`, language_id `319002153`.

Define and evaluate a string function in the historical dialect ReasonLIGO.

## Toolchain and reproduction

Required genuine ligo compiler/runtime, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Requires a LIGO release that supports ReasonLIGO; modern releases may have removed the frontend.

Comando/procedura from the directory of the example, unless explicit indications:

```text
ligo interpret result --init-file hello.religo --syntax reasonligo
```

Expected result: Hello, World! in output or compliant data, according to the scope described.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Funzione originale con parametro World; compiler storico unavailable. Nessuna catena, wallet o deployment necessario.

Remaining requirements:

- Required ligo compiler/runtime and matching host resources are not available/configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://gitlab.com/ligolang/ligo/-/tree/dev/src/test/contracts](https://gitlab.com/ligolang/ligo/-/tree/dev/src/test/contracts)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.religo` | [hello.religo](hello.religo) created; verification pending |
