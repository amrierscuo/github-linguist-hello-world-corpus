# #721 Thrift

Compilare una struttura Thrift e conservare la costante del saluto.

## Toolchain

Thrift version 0.19.0

## Procedura

thrift --gen py -out build hello.thrift; controllare corpus/constants.py generato con HELLO.

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.

Il compiler originale genera Python; la verifica legge la vera costante dal modulo generato.

Verifica reale 2026-10-08T13:30:04.884795+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://thrift.apache.org/docs/idl](https://thrift.apache.org/docs/idl)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.thrift` | [hello.thrift](hello.thrift) verificato |
