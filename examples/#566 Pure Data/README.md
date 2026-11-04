# #566 Pure Data

Load a Pure Data patch and print the loadbang message.

## Toolchain

Pd-0.54.1 ("") compiled for Debian (0.54.1+ds-4build3) on 2024/04/07 at 07:21:28 UTC

## Procedure

pd -nogui -noaudio -batch hello.pd

## Expected result

Console contains greeting: Hello, World!.

## Status

syntax and behavior verified.

Objects and connections are original; no audio/device. delay sends pd quit to finish the test.

Real check 2026-10-08T13:16:51.553751+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://github.com/pure-data/pure-data](https://github.com/pure-data/pure-data)
- [https://msp.ucsd.edu/Pd_documentation/](https://msp.ucsd.edu/Pd_documentation/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pd` | [hello.pd](hello.pd) verified |
