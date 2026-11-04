# #531 Pep8

Voce canonica `Pep8`, tipo `programming`, language_id `840372442`.

Print a string finished from scratch in the educational simulator Pep/8.

## Toolchain and reproduction

Required genuine compiler/runtime, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

It requires the assembler/simulatore Pep/8 and its OS, not Pep/9 or a different CPU.

Comando/procedura from the directory of the example, unless explicit indications:

```text
Aprire hello.pep nel software Pep/8 ufficiale, Assemble, poi Run con il suo OS standard.
```

Expected result: The conformed result contains Hello, World!, according to the framework described.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Original source STRO direct, STOP and ASCII data after code; tools not available.

Remaining requirements:

- Required pep8 compiler/interpreter and matching host libraries are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.computersystemsbook.com/4th-edition/pep8/](https://www.computersystemsbook.com/4th-edition/pep8/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pep` | [hello.pep](hello.pep) created; verification pending |
