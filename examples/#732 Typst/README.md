# #732 Typst

Engage Typst greeting and read the text of the PDF product.

## Toolchain

typst 0.15.1 (9dfd3a08); pypdf6.9.2

## Procedure

typst compile hello.typ build/hello.pdf; python verify.py build/hello.pdf

## Expected result

Hello, World!

## Status

syntax and behavior verified.



Real check 2026-10-08T13:30:07.268985+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://typst.app/docs/tutorial/](https://typst.app/docs/tutorial/)
- [https://typst.app/docs/reference/text/](https://typst.app/docs/reference/text/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.typ` | [hello.typ](hello.typ) verified |
