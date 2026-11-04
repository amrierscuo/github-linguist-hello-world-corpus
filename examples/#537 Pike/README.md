# #537 Pike

Voce canonica `Pike`, tipo `programming`, language_id `287`.

Run a main Pike that format and writes greeting.

## Toolchain and reproduction

Genuine Pike language interpreter — Pike v8.0 release 1738 Copyright © 1994-2022 Linköping University; Pike comes with ABSOLUTELY NO WARRANTY; This is free software and you are; welcome to redistribute it under certain conditions; read the files; COPYING and COPYRIGHT in the Pike distribution for more details.. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Pike 8.0 release 1738 autentico. La distribuzione relocata usa PIKE_MODULE_PATH, PIKE_INCLUDE_PATH e -m master.pike, tutti registrati nel log.

Comando/procedura from the directory of the example, unless explicit indications:

```text
pike hello.pike
```

Expected result: The conformed result contains Hello, World!, according to the framework described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Original Runtime reads and performs the main; exact stdout.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://pike.lysator.liu.se/docs/man/](https://pike.lysator.liu.se/docs/man/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pike` | [hello.pike](hello.pike), [driver.pike](variants/pmod-c6f9853d/driver.pike) created; verification pending |
| `.pmod` | [hello.pmod](variants/pmod-c6f9853d/hello.pmod) created; verification pending |
