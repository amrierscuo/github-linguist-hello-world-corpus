# #394 LiveCode Script

Caricare uno stack script-only LiveCode e invocare helloWorld.

## Toolchain

LiveCode Script engine; versione da registrare

## Comandi e procedura

In LiveCode caricare lo stack script-only hello.livecodescript; invocare helloWorld dal Message Box sullo stack

## Risultato atteso

Handler put scrive Hello, World! nel Message Box.

## Stato

Sintassi e semantica in attesa.

script HelloWorld identifica uno stack script-only; il saluto è nel gestore originale. Il runtime/compatibilità della versione devono essere registrati prima del claim positivo.

Requisiti residui:
- Engine LiveCode non predisposto; caricamento stack e handler pending.

## Fonti primarie

- [https://docs.livecode.com/](https://docs.livecode.com/)
- [https://github.com/livecode/livecode](https://github.com/livecode/livecode)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.livecodescript` | [hello.livecodescript](hello.livecodescript) creato, verifiche pendenti |
