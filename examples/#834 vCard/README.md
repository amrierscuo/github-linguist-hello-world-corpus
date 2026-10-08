# #834 vCard

Leggere un vCard originale con CRLF e conservare FN nel roundtrip.

## Toolchain

CPython3.13.9; vobject0.9.9

## Procedura

pip install vobject; python verify.py

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.

CRLF reali e virgola escapata; nome e indirizzo example.invalid sono illustrativi. Parser vobject autentico, nessuna rubrica importata.

Verifica reale 2026-10-08T13:48:50.935305+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://www.rfc-editor.org/rfc/rfc2426](https://www.rfc-editor.org/rfc/rfc2426)
- [https://vobject.readthedocs.io/latest/](https://vobject.readthedocs.io/latest/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.vcf` | [hello.vcf](hello.vcf) verificato |
