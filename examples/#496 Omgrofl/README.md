# #496 Omgrofl

Interpretare assegnamenti Omgrofl e rofl per emettere i byte del saluto.

## Toolchain

Java openjdk 21.0.12.1 2026-08-18 LTS; OlegSmelov interpreter commit 6c621627b913771f3896c75ea8a27f06e34f2e65

## Procedura

Compilare src/omgrofl del tool con javac; java -cp <interpreter-classes> omgrofl.Main hello.omgrofl

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.

Programma originale: un registro lol viene assegnato ai codici ASCII, rofl emette i byte. Interprete community autentico, non parser costruito per questo corpus.

Verifica reale 2026-10-08T13:10:45.310605+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://github.com/OlegSmelov/omgrofl-interpreter](https://github.com/OlegSmelov/omgrofl-interpreter)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.omgrofl` | [hello.omgrofl](hello.omgrofl) verificato |
