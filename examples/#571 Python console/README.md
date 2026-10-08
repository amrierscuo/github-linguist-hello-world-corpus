# #571 Python console

Eseguire un transcript Python console con doctest.

## Toolchain

CPython Python 3.13.9

## Procedura

python verify.py

## Risultato atteso

2 test passed; Hello, World! corrisponde all’output atteso.

## Stato

Sintassi e semantica verificate.

doctest originale legge prompt >>> ed esegue entrambe le istruzioni, confrontando l’output.

Verifica reale 2026-10-08T13:17:20.095478+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://docs.python.org/3/library/doctest.html](https://docs.python.org/3/library/doctest.html)
