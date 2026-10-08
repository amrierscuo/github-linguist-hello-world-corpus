# #307 Idris

Tipizzare ed eseguire un main Idris che usa putStrLn.

## Toolchain

Idris; scegliere/registrare una versione compatibile con .idr

## Comandi e procedura

idris --check hello.idr; idris hello.idr -o build/hello; build/hello

## Risultato atteso

Tipo main : IO (); programma stampa Hello, World! più newline.

## Stato

Sintassi e semantica in attesa.

Il modulo Main e il tipo IO rendono concreto il goal. Questo campione semplice è documentato secondo Idris 1; un’eventuale migrazione Idris 2 dovrà registrare tool/backend effettivi.

Requisiti residui:
- Compilatore/backend Idris non disponibili in questa tranche; type check e runtime pending.

## Fonti primarie

- [https://docs.idris-lang.org/en/latest/tutorial/introduction.html](https://docs.idris-lang.org/en/latest/tutorial/introduction.html)
- [https://docs.idris-lang.org/en/latest/tutorial/starting.html](https://docs.idris-lang.org/en/latest/tutorial/starting.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.idr` | [hello.idr](hello.idr) creato, verifiche pendenti |
| `.lidr` | [hello.lidr](variants/lidr-f41f21bf/hello.lidr) creato, verifiche pendenti |
