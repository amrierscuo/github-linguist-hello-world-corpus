# #529 Pascal

Voce canonica `Pascal`, tipo `programming`, language_id `281`.

Fill in and run a Pascal program with WriteLn.

## Toolchain and reproduction

Genuine Free Pascal compiler, 3.2.2. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Free Pascal 3.2.2 official; compiler and units RTL extracted under work.

Comando/procedura from the directory of the example, unless explicit indications:

```text
fpc -FEbuild -FUbuild hello.pas; build/hello
```

Expected result: The conformed result contains Hello, World!, according to the framework described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Genuine Compiler generates a native program that prints exactly the greeting.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.freepascal.org/docs.html](https://www.freepascal.org/docs.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pas` | [hello.pas](hello.pas), [driver.pas](variants/inc-dd126fb7/driver.pas) created; verification pending |
| `.dfm` | [hello.dfm](variants/dfm-e05beb09/hello.dfm) created; verification pending |
| `.dpr` | [hello.dpr](variants/dpr-30850e89/hello.dpr) created; verification pending |
| `.inc` | [hello.inc](variants/inc-dd126fb7/hello.inc) created; verification pending |
| `.lpr` | [hello.lpr](variants/lpr-3e546050/hello.lpr) created; verification pending |
| `.pascal` | [hello.pascal](variants/pascal-539d0d7d/hello.pascal) created; verification pending |
| `.pp` | [hello.pp](variants/pp-60aacc63/hello.pp) created; verification pending |
