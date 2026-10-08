# #808 Zimpl

Generare e risolvere un LP Zimpl il cui ottimo codifica i byte del saluto.

## Toolchain

Zimpl; LP solver

## Procedura

zimpl -o build/hello hello.zpl; glpsol --lp build/hello.lp; leggere e decodificare gli x[i] ottimali.

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica in attesa.

Variabili indicizzate originali hanno bounds [ASCII,ASCII+1]; l’obiettivo minimizzante deve scegliere i codici inferiori.

Requisiti residui:
- Zimpl compiler non disponibile nei pacchetti isolati; parsing/generazione LP e soluzione pending.

## Fonti primarie

- [https://zimpl.zib.de/](https://zimpl.zib.de/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.zimpl` | [hello.zimpl](variants/zimpl-c607d319/hello.zimpl) creato, verifiche pendenti |
| `.zmpl` | [hello.zmpl](variants/zmpl-c5eac23d/hello.zmpl) creato, verifiche pendenti |
| `.zpl` | [hello.zpl](hello.zpl) creato, verifiche pendenti |
