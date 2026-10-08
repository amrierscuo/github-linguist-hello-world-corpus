# #481 OASv2-json

Validare il contratto OpenAPI e la risposta di un consumer HTTP locale.

## Toolchain

Node.js v22.20.0; {'@apidevtools/swagger-parser': '13.1.0', 'ajv': '8.20.0'}

## Procedura

npm install; node verify.cjs hello.json

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.

Il parser originale valida e dereferenzia il documento; Ajv valida lo schema e respinge un saluto diverso. HTTP loopback consuma l’esempio del contratto. example.invalid è soltanto metadata; nessun servizio esterno viene contattato.

Verifica reale 2026-10-08T13:10:39.706920+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://spec.openapis.org/oas/v2.0.html](https://spec.openapis.org/oas/v2.0.html)
- [https://apidevtools.com/swagger-parser/](https://apidevtools.com/swagger-parser/)
- [https://ajv.js.org/](https://ajv.js.org/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.json` | [hello.json](hello.json), [package.json](package.json) verificato |
