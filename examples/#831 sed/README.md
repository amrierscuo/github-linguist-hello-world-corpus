# #831 sed

Perform replacement in the sed program.

## Toolchain

sed (GNU sed) 4.9

## Procedure

sed -f hello.sed input.txt

## Expected result

Hello, World!

## Status

syntax and behavior verified.



Real check 2026-10-08T13:48:50.567949+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://www.gnu.org/software/sed/manual/sed.html](https://www.gnu.org/software/sed/manual/sed.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.sed` | [hello.sed](hello.sed) verified |
