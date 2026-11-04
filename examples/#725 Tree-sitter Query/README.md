# #725 Tree-sitter Query

Fill a Tree-sitter query and capture the greeting string from the real AST Python.

## Toolchain

CPython3.13.9; tree-sitter0.26.0/tree-sitter-python0.25.0

## Procedure

pip install tree-sitter tree-sitter-python; python verify.py

## Expected result

Hello, World!

## Status

syntax and behavior verified.

Parser and QueryCursor engine are the original ones; they control catching the caller and string.

Real check 2026-10-08T13:30:04.904502+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://tree-sitter.github.io/tree-sitter/using-parsers/queries/1-syntax.html](https://tree-sitter.github.io/tree-sitter/using-parsers/queries/1-syntax.html)
- [https://tree-sitter.github.io/py-tree-sitter/](https://tree-sitter.github.io/py-tree-sitter/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.scm` | [hello.scm](hello.scm) verified |
