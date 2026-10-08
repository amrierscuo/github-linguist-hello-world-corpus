# #490 Object Data Instance Notation

Decodificare l’attributo greeting ODIN di openEHR.

## Toolchain

Parser ODIN openEHR conforme

## Procedura

Caricare hello.odin con un parser ODIN openEHR e leggere greeting; registrare API/versione/risultato.

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica in attesa.

ODIN è Object Data Instance Notation di openEHR; il valore primitivo stringa è racchiuso in < >. Non contiene dati di pazienti.

Requisiti residui:
- Parser ODIN openEHR non predisposto.

## Fonti primarie

- [https://specifications.openehr.org/releases/BASE/latest/odin.html](https://specifications.openehr.org/releases/BASE/latest/odin.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.odin` | [hello.odin](hello.odin) creato, verifiche pendenti |
