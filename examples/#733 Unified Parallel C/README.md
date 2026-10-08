# #733 Unified Parallel C

Compilare Unified Parallel C e stampare da un solo thread.

## Toolchain

UPC compiler/runtime

## Procedura

upcc -o build/hello hello.upc; upcrun -n 2 build/hello

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica in attesa.



Requisiti residui:
- UPC compiler e runtime shared-memory non predisposti.

## Fonti primarie

- [https://upc.lbl.gov/docs/](https://upc.lbl.gov/docs/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.upc` | [hello.upc](hello.upc) creato, verifiche pendenti |
