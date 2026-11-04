# #161 Daslang

Stampare Hello, World! e newline da main esportata in Daslang gen2.

## Toolchain

Official Daslang 0.6.4 Windows portable bundle

## Commands and procedure

daslang --version; daslang hello.das

## Expected result

Exit 0; stdout exactly Hello, World! plus newline.

## Status

syntax and behavior verified.

The syntax gen2 uses braces and [export] for main. print does not add newline: the source specifies it. The official bundle contains interpreters and modules; it is used its track directly.

Actual verification of 2026-10-08T11:56:15.636441+00:00 on Windows x64: [log](verification/result.json).
Hash of sorgenti/checker, real versions and commands, output codes, stdout/stderr and test limits are in the log.

## Primary sources and format reference

- [https://daslang.io/doc/reference/tutorials/01_hello_world.html](https://daslang.io/doc/reference/tutorials/01_hello_world.html)
- [https://github.com/GaijinEntertainment/daScript/releases/tag/v0.6.4](https://github.com/GaijinEntertainment/daScript/releases/tag/v0.6.4)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.das` | [hello.das](hello.das) verified |
