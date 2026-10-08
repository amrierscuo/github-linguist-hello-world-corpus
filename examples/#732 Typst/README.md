# #732 Typst

Impaginare il saluto Typst e leggere il testo del PDF prodotto.

## Toolchain

typst 0.15.1 (9dfd3a08); pypdf6.9.2

## Procedura

typst compile hello.typ build/hello.pdf; python verify.py build/hello.pdf

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.



Verifica reale 2026-10-08T13:30:07.268985+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://typst.app/docs/tutorial/](https://typst.app/docs/tutorial/)
- [https://typst.app/docs/reference/text/](https://typst.app/docs/reference/text/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.typ` | [hello.typ](hello.typ) verificato |
