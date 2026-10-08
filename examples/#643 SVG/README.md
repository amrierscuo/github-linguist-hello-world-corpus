# #643 SVG

Renderizzare il saluto SVG in Chromium.

## Toolchain

Google Chrome 154.0.8037.98 native SVG renderer

## Procedura

Chrome --headless --screenshot=build/hello.png hello.svg; controllare testo e immagine.

## Risultato atteso

SVG mostra Hello, World! su sfondo chiaro.

## Stato

Sintassi e semantica verificate.

SVG originale con nodo text; nessun font incorporato. Il browser interpreta il vero SVG e produce uno screenshot.

Verifica reale 2026-10-08T13:23:05.345487+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://www.w3.org/TR/SVG2/text.html](https://www.w3.org/TR/SVG2/text.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.svg` | [hello.svg](hello.svg) verificato |
