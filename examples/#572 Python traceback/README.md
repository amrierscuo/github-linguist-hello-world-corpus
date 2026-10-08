# #572 Python traceback

Generare un traceback CPython reale contenente il saluto.

## Toolchain

CPython Python 3.13.9

## Procedura

python hello.py; confrontare stderr normalizzato con hello.pytb

## Risultato atteso

Traceback reale termina con RuntimeError: Hello, World!, exit 1.

## Stato

Sintassi e semantica verificate.

Il codice solleva intenzionalmente RuntimeError; exit 1 è atteso. hello.pytb viene generato dal vero interprete, normalizzando soltanto il percorso del file.

Verifica reale 2026-10-08T13:16:51.286983+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://docs.python.org/3/library/traceback.html](https://docs.python.org/3/library/traceback.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pytb` | [hello.pytb](hello.pytb) verificato |
