# #833 ucode

Interpret ucode with concatenation of greeting.

## Toolchain

ucode upstream 0102932915ffb494e5ed61459161a2cba0512226; GCC13.3.0; json-c0.17

## Procedure

ucode hello.uc

## Expected result

Hello, World!

## Status

syntax and behavior verified.



Real check 2026-10-08T13:49:04.191479+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://github.com/ucode-lang/ucode](https://github.com/ucode-lang/ucode)
- [https://ucode-lang.org/](https://ucode-lang.org/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.uc` | [hello.uc](hello.uc) verified |
