# #564 Pug

Renderizzare una pagina Pug con interpolazione ed escaping.

## Toolchain

Pug 3.0.4; Node.js v22.20.0

## Procedura

npm install pug; node verify.cjs

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.

Il compilatore Pug originale produce HTML e il checker controlla il nodo del saluto e l’escaping del nome.

Verifica reale 2026-10-08T13:16:51.001660+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://pugjs.org/api/getting-started.html](https://pugjs.org/api/getting-started.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.jade` | [hello.jade](variants/jade-6d41832d/hello.jade) creato, verifiche pendenti |
| `.pug` | [hello.pug](hello.pug) verificato |
