# #255 Gno

Eseguire un main Gno che stampa Hello, World! con println.

## Toolchain

gno version: v1.5.0

## Comandi e procedura

gno version; gno run hello.gno

## Risultato atteso

GnoVM interpreta il file; Hello, World! più newline, exit 0.

## Stato

Sintassi e semantica verificate.

La verifica usa il CLI originale che esegue GnoVM, non il compilatore Go su una sorgente rinominata. Il programma locale non pubblica package sulla blockchain e non esegue transazioni.

Verifica effettiva del 2026-10-08T12:15:44.133484+00:00 su WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://github.com/gnolang/gno](https://github.com/gnolang/gno)
- [https://github.com/gnolang/gno/releases/tag/v1.5.0](https://github.com/gnolang/gno/releases/tag/v1.5.0)
- [https://docs.gno.land/](https://docs.gno.land/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.gno` | [hello.gno](hello.gno) verificato |
