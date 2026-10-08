# #729 Type Language

Compilare un costruttore nel Type Language TL di Telegram.

## Toolchain

TL compiler e runtime generato

## Procedura

Compilare hello.tl con un tool TL compatibile; costruire Greeting(text="Hello, World!") e verificare roundtrip.

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica in attesa.

Lo schema non inventa un constructor ID: il compilatore deve calcolarlo dal costruttore canonico.

Requisiti residui:
- Compiler TL/runtime per schema originale non predisposti.

## Fonti primarie

- [https://core.telegram.org/mtproto/TL](https://core.telegram.org/mtproto/TL)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.tl` | [hello.tl](hello.tl) creato, verifiche pendenti |
