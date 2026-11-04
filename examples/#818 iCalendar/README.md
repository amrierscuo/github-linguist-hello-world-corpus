# #818 iCalendar

Analyze an original iCalendar event and keep your greeting in roundtrip.

## Toolchain

CPython3.13.9; icalendar7.3.0

## Procedure

pip install icalendar; python verify.py

## Expected result

Hello, World!

## Status

syntax and behavior verified.

UID usa example.invalid; nessun evento viene importato in calendari reali. Il parser decodifica l’escaping della virgola e preserva Summary/date.

Real check 2026-10-08T13:38:35.257218+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://www.rfc-editor.org/rfc/rfc5545](https://www.rfc-editor.org/rfc/rfc5545)
- [https://icalendar.readthedocs.io/](https://icalendar.readthedocs.io/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ics` | [hello.ics](hello.ics) verified |
| `.ical` | [hello.ical](variants/ical-1b64d378/hello.ical) created; verification pending |
