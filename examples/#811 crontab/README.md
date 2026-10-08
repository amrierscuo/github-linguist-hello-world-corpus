# #811 crontab

Analizzare una riga crontab ed eseguire soltanto il suo comando nel fixture locale.

## Toolchain

CPython3.13.9; python-crontab3.4.0

## Procedura

pip install python-crontab; python verify.py

## Risultato atteso

Schedule 0 9 * * * valida; comando emette Hello, World!.

## Stato

Sintassi e semantica verificate.

Il parser esistente legge orario e comando; il comando viene provato una volta. Nessun cron viene installato o pianificato.

Verifica reale 2026-10-08T13:38:34.781824+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://man7.org/linux/man-pages/man5/crontab.5.html](https://man7.org/linux/man-pages/man5/crontab.5.html)
- [https://gitlab.com/doctormo/python-crontab](https://gitlab.com/doctormo/python-crontab)
