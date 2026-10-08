# #738 Untyped Plutus Core

Analizzare e valutare una costante stringa Untyped Plutus Core.

## Toolchain

UPLC parser/CEK evaluator

## Procedura

Usare il parser/evaluatore UPLC ufficiale della versione compatibile per valutare hello.uplc.

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica in attesa.

Il programma è una costante, senza transazioni o deployment.

Requisiti residui:
- Toolchain UPLC/CEK non predisposta; valutazione pending.

## Fonti primarie

- [https://plutus.cardano.intersectmbo.org/docs/](https://plutus.cardano.intersectmbo.org/docs/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.uplc` | [hello.uplc](hello.uplc) creato, verifiche pendenti |
