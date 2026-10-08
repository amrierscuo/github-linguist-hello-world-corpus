# #833 ucode

Interpretare ucode con concatenazione del saluto.

## Toolchain

ucode upstream 0102932915ffb494e5ed61459161a2cba0512226; GCC13.3.0; json-c0.17

## Procedura

ucode hello.uc

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.



Verifica reale 2026-10-08T13:49:04.191479+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://github.com/ucode-lang/ucode](https://github.com/ucode-lang/ucode)
- [https://ucode-lang.org/](https://ucode-lang.org/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.uc` | [hello.uc](hello.uc) verificato |
