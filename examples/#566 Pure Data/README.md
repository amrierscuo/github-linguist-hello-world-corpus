# #566 Pure Data

Caricare un patch Pure Data e stampare il messaggio del loadbang.

## Toolchain

Pd-0.54.1 ("") compiled for Debian (0.54.1+ds-4build3) on 2024/04/07 at 07:21:28 UTC

## Procedura

pd -nogui -noaudio -batch hello.pd

## Risultato atteso

Console contiene greeting: Hello, World!.

## Stato

Sintassi e semantica verificate.

Oggetti e connessioni sono originali; niente audio/device. delay invia pd quit per terminare il test.

Verifica reale 2026-10-08T13:16:51.553751+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://github.com/pure-data/pure-data](https://github.com/pure-data/pure-data)
- [https://msp.ucsd.edu/Pd_documentation/](https://msp.ucsd.edu/Pd_documentation/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pd` | [hello.pd](hello.pd) verificato |
