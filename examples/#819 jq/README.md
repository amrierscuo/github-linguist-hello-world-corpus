# #819 jq

Eseguire il filtro jq sul nome del fixture JSON.

## Toolchain

jq-1.7

## Procedura

jq -r -f hello.jq input.json

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.



Verifica reale 2026-10-08T13:38:35.952725+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://jqlang.org/manual/](https://jqlang.org/manual/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.jq` | [hello.jq](hello.jq) verificato |
