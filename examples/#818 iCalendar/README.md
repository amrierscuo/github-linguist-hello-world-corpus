# #818 iCalendar

Analizzare un evento iCalendar originale e conservare il saluto nel roundtrip.

## Toolchain

CPython3.13.9; icalendar7.3.0

## Procedura

pip install icalendar; python verify.py

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.

UID usa example.invalid; nessun evento viene importato in calendari reali. Il parser decodifica l’escaping della virgola e preserva Summary/date.

Verifica reale 2026-10-08T13:38:35.257218+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://www.rfc-editor.org/rfc/rfc5545](https://www.rfc-editor.org/rfc/rfc5545)
- [https://icalendar.readthedocs.io/](https://icalendar.readthedocs.io/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ics` | [hello.ics](hello.ics) verificato |
| `.ical` | [hello.ical](variants/ical-1b64d378/hello.ical) creato, verifiche pendenti |
