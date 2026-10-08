# #396 Lobster

Compilare ed eseguire Lobster per stampare il saluto.

## Toolchain

Official aardappel Lobster release v2026.8 Windows x64

## Comandi e procedura

lobster --help; lobster --no-crash-dialog hello.lobster

## Risultato atteso

Compiler/VM originali accettano print; stdout Hello, World! più newline; exit 0.

## Stato

Sintassi e semantica verificate.

Lobster è il linguaggio di Wouter van Oortmerssen (aardappel); il log registra anche l’hash del vero engine. Non si tratta di altri prodotti omonimi.

Verifica effettiva del 2026-10-08T12:49:26.320562+00:00 su Windows x64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://aardappel.github.io/lobster/getting_started.html](https://aardappel.github.io/lobster/getting_started.html)
- [https://github.com/aardappel/lobster/releases/tag/v2026.8](https://github.com/aardappel/lobster/releases/tag/v2026.8)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.lobster` | [hello.lobster](hello.lobster) verificato |
