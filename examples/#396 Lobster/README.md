# #396 Lobster

Fill out and execute Lobster to print your greeting.

## Toolchain

Official aardappel Lobster release v2026.8 Windows x64

## Commands and procedure

lobster --help; lobster --no-crash-dialog hello.lobster

## Expected result

Compiler/VM original accept print; stdout Hello, World! plus newline; exit 0.

## Status

syntax and behavior verified.

Lobster è il linguaggio di Wouter van Oortmerssen (aardappel); il log registra anche l’hash del vero engine. Non si tratta di altri prodotti omonimi.

Actual verification of 2026-10-08T12:49:26.320562+00:00 on Windows x64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://aardappel.github.io/lobster/getting_started.html](https://aardappel.github.io/lobster/getting_started.html)
- [https://github.com/aardappel/lobster/releases/tag/v2026.8](https://github.com/aardappel/lobster/releases/tag/v2026.8)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.lobster` | [hello.lobster](hello.lobster) verified |
