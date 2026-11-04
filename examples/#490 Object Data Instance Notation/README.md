# #490 Object Data Instance Notation

Decode the greeting ODIN attribute of openEHR.

## Toolchain

Parser ODIN openEHR conforme

## Procedure

Upload hello.odin with a parser ODIN openEHR and read greeting; record API/versione/risultato.

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.

ODIN is Object Data Instance Notation of openEHR; the primitive string value is enclosed in < >. It does not contain patient data.

Remaining requirements:
- Parser ODIN openEHR not predisposed.

## Primary sources

- [https://specifications.openehr.org/releases/BASE/latest/odin.html](https://specifications.openehr.org/releases/BASE/latest/odin.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.odin` | [hello.odin](hello.odin) created; verification pending |
