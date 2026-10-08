# #573 Q#

Eseguire una entry point Q# classica che invoca Message.

## Toolchain

Q# compiler/runtime compatibile

## Procedura

Compilare Main.qs con toolchain Q# che supporta @EntryPoint e registrare l’esecuzione locale.

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica in attesa.



Requisiti residui:
- Q# compiler/runtime locale non predisposto; compatibilità entry-point da registrare.

## Fonti primarie

- [https://learn.microsoft.com/azure/quantum/user-guide/language/statements/calls](https://learn.microsoft.com/azure/quantum/user-guide/language/statements/calls)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.qs` | [Main.qs](Main.qs) creato, verifiche pendenti |
