# #725 Tree-sitter Query

Compilare una query Tree-sitter e catturare la stringa del saluto dal vero AST Python.

## Toolchain

CPython3.13.9; tree-sitter0.26.0/tree-sitter-python0.25.0

## Procedura

pip install tree-sitter tree-sitter-python; python verify.py

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.

Parser e motore QueryCursor sono quelli originali; si controllano cattura del chiamante e della stringa.

Verifica reale 2026-10-08T13:30:04.904502+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://tree-sitter.github.io/tree-sitter/using-parsers/queries/1-syntax.html](https://tree-sitter.github.io/tree-sitter/using-parsers/queries/1-syntax.html)
- [https://tree-sitter.github.io/py-tree-sitter/](https://tree-sitter.github.io/py-tree-sitter/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.scm` | [hello.scm](hello.scm) verificato |
