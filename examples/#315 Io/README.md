# #315 Io

Inviare println a una stringa nel runtime Io.

## Toolchain

IoLanguage Io; versione da registrare

## Comandi e procedura

io hello.io

## Risultato atteso

Hello, World! più newline; exit 0.

## Stato

Sintassi e semantica in attesa.

Il programma usa il dispatch a messaggi di Io e il metodo println della stringa. Nessuna traduzione ad altri linguaggi è usata per contare la verifica.

Requisiti residui:
- Interprete Io nativo non preparato; parsing/evaluation pending.

## Fonti primarie

- [https://iolanguage.org/docs/Tutorial/index.html](https://iolanguage.org/docs/Tutorial/index.html)
- [https://github.com/IoLanguage/io](https://github.com/IoLanguage/io)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.io` | [hello.io](hello.io) creato, verifiche pendenti |
