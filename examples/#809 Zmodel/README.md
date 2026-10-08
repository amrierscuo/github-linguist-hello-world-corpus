# #809 Zmodel

Analizzare uno schema Zmodel con default del saluto.

## Toolchain

ZenStack2.22.3; Node22.20.0

## Procedura

zenstack check --schema hello.zmodel; generare/applicare il modello SQLite nel progetto di prova e verificare il default di message

## Risultato atteso

Hello, World!

## Stato

Sintassi verificata; semantica in attesa.

Lo schema usa il dialetto ZenStack2; la policy allow è illustrativa per dati locali di esempio.

Verifica reale 2026-10-08T13:40:45.878337+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

Requisiti residui:
- ORM generation/SQLite default runtime pending.

## Fonti primarie

- [https://github.com/zenstackhq/zenstack/tree/v2.22.3](https://github.com/zenstackhq/zenstack/tree/v2.22.3)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.zmodel` | [hello.zmodel](hello.zmodel) sintassi verificata |
