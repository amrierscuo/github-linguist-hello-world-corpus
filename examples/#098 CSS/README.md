# #098 CSS

Generare Hello, World! nel pseudo-elemento CSS ::before di .hello e applicare il colore #123456 nella pagina di supporto.

## Toolchain

Node.js v22.20.0; css-tree 3.2.1; Google Chrome 154.0.8037.98 (installed file ProductVersion)

## Comandi e procedura

Da questa cartella:

```sh
npm install
node check.cjs
```

Aprire hello.html nel browser. Lo script della pagina legge gli stili
calcolati di ::before e li rende ispezionabili negli attributi data-* del body.
Nel test Chrome è stato avviato in modalità headless con profilo temporaneo;
il DOM finale prova il valore content e il colore calcolato. La stringa
generata deve provenire dalla regola CSS, non dal testo del paragrafo HTML.

## Risultato atteso

Parser senza errori e dichiarazioni valide; browser risolve content="Hello, World!" e color=rgb(18, 52, 86).

## Stato

Sintassi e semantica verificate.

hello.html carica il CSS e registra i valori effettivi del browser in data-generated-content e data-generated-color. La verifica usa Chrome reale con profilo temporaneo, oltre al parser CSS Tree; non dichiara un confronto di screenshot.

Verifica effettiva del 2026-10-08T11:33:51.391848+00:00 su Windows x64: [log](verification/result.json).
Il log include hash SHA-256 della sorgente e dei checker, versioni, comandi, codici di uscita, stdout, stderr e limiti della prova.

## Fonti primarie

- [https://github.com/csstree/csstree](https://github.com/csstree/csstree)
- [https://www.w3.org/TR/css-content-3/](https://www.w3.org/TR/css-content-3/)
- [https://developer.chrome.com/docs/chromium/headless](https://developer.chrome.com/docs/chromium/headless)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.css` | [hello.css](hello.css) verificato |
