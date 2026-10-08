# #251 Glimmer JS

Definire un componente template-only Glimmer JS con titolo Hello, World!.

## Toolchain

Node.js v22.20.0; content-tag 4.2.1, @glimmer/syntax 0.95.0, @babel/core 8.0.7, @babel/preset-typescript 8.0.7

## Comandi e procedura

npm install; node check.cjs; integrare hello.gjs come componente in un’app Ember compatibile e renderizzarlo

## Risultato atteso

Parser accetta template-tag e JavaScript generato; runtime Ember rende <h1>Hello, World!</h1>.

## Stato

Sintassi verificata; semantica in attesa.

content-tag usa il preprocessore Rust/SWC in WASM; Glimmer analizza il template e Babel il codice ospite generato. Il titolo nel template AST è verificato. Questa prova di compilazione/parsing non attesta il rendering del componente Ember, che resta pending.

Verifica effettiva del 2026-10-08T12:17:25.190660+00:00 su Windows x64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

Requisiti residui:
- Ember application/runtime DOM rendering not yet performed.

## Fonti primarie

- [https://github.com/ember-cli/ember-template-imports](https://github.com/ember-cli/ember-template-imports)
- [https://github.com/embroider-build/content-tag](https://github.com/embroider-build/content-tag)
- [https://github.com/glimmerjs/glimmer-vm](https://github.com/glimmerjs/glimmer-vm)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.gjs` | [hello.gjs](hello.gjs) sintassi verificata |
