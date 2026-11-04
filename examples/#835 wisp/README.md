# #835 wisp

Play Wisp as syntax indented Scheme.

## Toolchain

guile (GNU Guile) 3.0.9; original Wisp1.0.13 reader

## Procedure

guile --language=wisp hello.wisp after configuring the original Wisp reader.

## Expected result

Hello, World!

## Status

syntax and behavior verified.

Two original expressions equal to (display...) and (newline); it serves the authentic Wisp reader.

Real check 2026-10-08T13:50:50.760897+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://www.draketo.de/software/wisp](https://www.draketo.de/software/wisp)
- [https://www.draketo.de/proj/wisp/](https://www.draketo.de/proj/wisp/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.wisp` | [hello.wisp](hello.wisp) verified |
