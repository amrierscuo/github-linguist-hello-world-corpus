# #642 STON

Leggere una mappa STON in Smalltalk.

## Toolchain

STON originale su Pharo/Squeak

## Procedura

STON fromString: (FileSystem workingDirectory / 'hello.ston') contents; leggere la chiave greeting.

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica in attesa.



Requisiti residui:
- VM Smalltalk e libreria STON non predisposte.

## Fonti primarie

- [https://github.com/svenvc/ston/blob/master/ston-spec.md](https://github.com/svenvc/ston/blob/master/ston-spec.md)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ston` | [hello.ston](hello.ston) creato, verifiche pendenti |
