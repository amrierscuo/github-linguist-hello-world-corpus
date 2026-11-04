# #727 Turtle

Read a triple Turtle and recover the literal greeting.

## Toolchain

CPython3.13.9; RDFLib7.6.0

## Procedure

pip install rdflib; python verify.py

## Expected result

Hello, World!

## Status

syntax and behavior verified.

RDFLib parser authentic; IRIs are illustrative identifiers without network requests.

Real check 2026-10-08T13:30:05.471503+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://www.w3.org/TR/turtle/](https://www.w3.org/TR/turtle/)
- [https://rdflib.readthedocs.io/](https://rdflib.readthedocs.io/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ttl` | [hello.ttl](hello.ttl) verified |
