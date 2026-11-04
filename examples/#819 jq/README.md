# #819 jq

Run the jq filter on the JSON fixture name.

## Toolchain

jq-1.7

## Procedure

jq -r -f hello.jq input.json

## Expected result

Hello, World!

## Status

syntax and behavior verified.



Real check 2026-10-08T13:38:35.952725+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://jqlang.org/manual/](https://jqlang.org/manual/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.jq` | [hello.jq](hello.jq) verified |
