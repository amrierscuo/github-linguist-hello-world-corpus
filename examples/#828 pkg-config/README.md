# #828 pkg-config

## Latest recorded verification

Latest extension checks:
- `.pc.in`: Native CMake configured the original pkg-config template with its documented prefix/version. The genuine pkg-config consumer read greeting=Hello, World!, version 1.0.0 and prefix /corpus/example from the generated metadata, using only an isolated package search directory. [Evidence](verification/native_20261105_batch_2e70632e696e.json).

Read metadata pkg-config and greeting variable.

## Toolchain

pkg-config 1.8.1

## Procedure

PKG_CONFIG_PATH =<cartella-assoluta> pkg-config --validate hello; pkg-config --variable=greeting hello

## Expected result

Hello, World!

## Status

syntax and behavior verified.

The library is illustrative: Libs/Cflags blanks. pkg-config controls the file and really solves the greeting variable; you don't look for an invented library.

Real check 2026-10-08T13:48:50.733718+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://people.freedesktop.org/~dbn/pkg-config-guide.html](https://people.freedesktop.org/~dbn/pkg-config-guide.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pc` | [hello.pc](hello.pc) verified |
| `.pc.in` | [hello.pc.in](variants/pc-in-477d8206/hello.pc.in) syntax and behavior verified |