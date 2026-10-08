# #835 wisp

Interpretare Wisp come sintassi indentata Scheme.

## Toolchain

guile (GNU Guile) 3.0.9; original Wisp1.0.13 reader

## Procedura

guile --language=wisp hello.wisp dopo aver configurato il reader Wisp originale.

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.

Due espressioni originali equivalgono a (display ...) e (newline); serve il reader Wisp autentico.

Verifica reale 2026-10-08T13:50:50.760897+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://www.draketo.de/software/wisp](https://www.draketo.de/software/wisp)
- [https://www.draketo.de/proj/wisp/](https://www.draketo.de/proj/wisp/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.wisp` | [hello.wisp](hello.wisp) verificato |
