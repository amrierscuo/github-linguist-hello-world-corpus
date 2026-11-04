# #255 Gno

Run a main Gno printing Hello, World! with println.

## Toolchain

gno version: v1.5.0

## Commands and procedure

gno version; gno run hello.gno

## Expected result

GnoVM interprets the file; Hello, World! plus newline, exit 0.

## Status

syntax and behavior verified.

The verification uses the original CLI running GnoVM, not the Go compiler on a renamed source.

Actual verification of 2026-10-08T12:15:44.133484+00:00 on WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://github.com/gnolang/gno](https://github.com/gnolang/gno)
- [https://github.com/gnolang/gno/releases/tag/v1.5.0](https://github.com/gnolang/gno/releases/tag/v1.5.0)
- [https://docs.gno.land/](https://docs.gno.land/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.gno` | [hello.gno](hello.gno) verified |
