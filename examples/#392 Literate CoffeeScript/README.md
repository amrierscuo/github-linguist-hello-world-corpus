# #392 Literate CoffeeScript

Compilare codice indentato in un documento Literate CoffeeScript e stampare il saluto.

## Toolchain

coffeescript 2.7.0; Node 22.20.0

## Comandi e procedura

npm install; npx coffee hello.litcoffee

## Risultato atteso

Prosa ignorata, codice indentato compilato; stdout Hello, World! più newline.

## Stato

Sintassi e semantica verificate.

Il formato .litcoffee viene riconosciuto dal compilatore ufficiale; l’esecuzione sul runtime Node è reale. Non si estrae manualmente il blocco per contare la verifica.

Verifica effettiva del 2026-10-08T12:48:17.110423+00:00 su Windows x64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://coffeescript.org/#literate](https://coffeescript.org/#literate)
- [https://github.com/jashkenas/coffeescript](https://github.com/jashkenas/coffeescript)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.litcoffee` | [hello.litcoffee](hello.litcoffee) verificato |
| `.coffee.md` | [hello.coffee.md](variants/coffee-md-862b0193/hello.coffee.md) creato, verifiche pendenti |
