# #834 vCard

Read an original vCard with CRLF and store FN in roundtrip.

## Toolchain

CPython3.13.9; vobject0.9.9

## Procedure

pip install vobject; python verify.py

## Expected result

Hello, World!

## Status

syntax and behavior verified.

CRLF real and emptied comma; name and address example.invalid are illustrative. Authentic parser vobject, no imported column.

Real check 2026-10-08T13:48:50.935305+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://www.rfc-editor.org/rfc/rfc2426](https://www.rfc-editor.org/rfc/rfc2426)
- [https://vobject.readthedocs.io/latest/](https://vobject.readthedocs.io/latest/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.vcf` | [hello.vcf](hello.vcf) verified |
