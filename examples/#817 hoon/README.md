# #817 hoon

Valutare una stringa Hoon nel gate di un generatore say.

## Toolchain

Urbit Hoon compiler/dojo

## Procedura

Inserire hello.hoon nel pier di prova come gen/hello.hoon e invocare +hello nel dojo.

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica in attesa.

Struttura say generator originale: gate esterno produce %say e gate interno restituisce un %noun cord.

Requisiti residui:
- Urbit pier/compiler Hoon non disponibile; type check del generatore e risultato pending.

## Fonti primarie

- [https://docs.urbit.org/hoon/](https://docs.urbit.org/hoon/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.hoon` | [hello.hoon](hello.hoon) creato, verifiche pendenti |
