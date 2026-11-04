# #815 edn

Read a EDN map with keyword and greeting string.

## Toolchain

CPython3.13.9; edn-format0.8.0

## Procedure

pip install edn-format; python verify.py

## Expected result

Hello, World!

## Status

syntax and behavior verified.

Parser community authentic EDN; the checker reads real keywords and does not use a parser written for the corpus.

Real check 2026-10-08T13:38:34.791457+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://github.com/edn-format/edn](https://github.com/edn-format/edn)
- [https://github.com/swaroopch/edn_format](https://github.com/swaroopch/edn_format)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.edn` | [hello.edn](hello.edn) verified |
