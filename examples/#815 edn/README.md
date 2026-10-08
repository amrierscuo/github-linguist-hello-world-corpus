# #815 edn

Leggere una mappa EDN con keyword e stringa del saluto.

## Toolchain

CPython3.13.9; edn-format0.8.0

## Procedura

pip install edn-format; python verify.py

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.

Parser community autentico EDN; il checker legge keyword reali e non usa un parser scritto per il corpus.

Verifica reale 2026-10-08T13:38:34.791457+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://github.com/edn-format/edn](https://github.com/edn-format/edn)
- [https://github.com/swaroopch/edn_format](https://github.com/swaroopch/edn_format)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.edn` | [hello.edn](hello.edn) verificato |
