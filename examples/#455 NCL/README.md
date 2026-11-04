# #455 NCL

Voce canonica `NCL`, tipo `programming`, language_id `240`.

Print a chained string in NCAR NCL.

## Toolchain and reproduction

Required genuine toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

It requires NCL and compatible NCAR scientific libraries. -Q suppresses banner, -n suppresses index in printed strings.

Comando/procedura from the directory of the example, unless explicit indications:

```text
ncl -Q -n hello.ncl
```

Expected result: Hello, World!

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Programma originale; runtime non configurato.

Remaining requirements:

- NCAR NCL interpreter and runtime libraries are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.ncl.ucar.edu/Document/Functions/Built-in/print.shtml](https://www.ncl.ucar.edu/Document/Functions/Built-in/print.shtml)
- [https://www.ncl.ucar.edu/Document/Manuals/Ref_Manual/NclStatements.shtml](https://www.ncl.ucar.edu/Document/Manuals/Ref_Manual/NclStatements.shtml)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ncl` | [hello.ncl](hello.ncl) created; verification pending |
