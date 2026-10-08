# #727 Turtle

Leggere una tripla Turtle e recuperare il literal del saluto.

## Toolchain

CPython3.13.9; RDFLib7.6.0

## Procedura

pip install rdflib; python verify.py

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.

RDFLib parser autentico; IRIs sono identificatori illustrativi senza richieste di rete.

Verifica reale 2026-10-08T13:30:05.471503+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://www.w3.org/TR/turtle/](https://www.w3.org/TR/turtle/)
- [https://rdflib.readthedocs.io/](https://rdflib.readthedocs.io/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ttl` | [hello.ttl](hello.ttl) verificato |
