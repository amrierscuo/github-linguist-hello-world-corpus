# #830 reStructuredText

Analizzare e renderizzare reStructuredText in HTML con enfasi.

## Toolchain

CPython3.13.9; Docutils0.23

## Procedure

pip install docutils; python verify.py

## Expected result

Hello, World!

## Status

syntax and behavior verified.

Doctree and writer HTML5 are those of original Docutils; they compare the text of the paragraph and strong greeting.

Real check 2026-10-08T13:48:50.865932+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.rst` | [hello.rst](hello.rst) verified |
| `.rest` | [hello.rest](variants/rest-90077caa/hello.rest) created; verification pending |
| `.rest.txt` | [hello.rest.txt](variants/rest-txt-4f6501d2/hello.rest.txt) created; verification pending |
| `.rst.txt` | [hello.rst.txt](variants/rst-txt-05b28309/hello.rst.txt) created; verification pending |
