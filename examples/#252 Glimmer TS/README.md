# #252 Glimmer TS

Definire un componente Glimmer TS con greeting tipizzato string e interpolazione nel titolo.

## Toolchain

Node.js v22.20.0; content-tag 4.2.1, @glimmer/syntax 0.95.0, @babel/core 8.0.7, @babel/preset-typescript 8.0.7

## Comandi e procedura

npm install; node check.cjs; integrare hello.gts in app Ember con Glint/TypeScript e renderizzarlo

## Risultato atteso

Parser accetta TypeScript/template-tag; Glint type check; runtime rende il titolo Hello, World!.

## Stato

Sintassi verificata; semantica in attesa.

SWC/content-tag e Babel TypeScript analizzano realmente il file; Glimmer risolve la struttura AST {{greeting}}. Babel rimuove l’annotazione ma non è un type checker completo. Type check Glint e DOM rendering Ember restano pending.

Verifica effettiva del 2026-10-08T12:17:25.882443+00:00 su Windows x64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

Requisiti residui:
- Ember application/runtime DOM rendering not yet performed.
- Glint/TypeScript full type check pending.

## Fonti primarie

- [https://github.com/ember-cli/ember-template-imports](https://github.com/ember-cli/ember-template-imports)
- [https://github.com/embroider-build/content-tag](https://github.com/embroider-build/content-tag)
- [https://typed-ember.gitbook.io/glint](https://typed-ember.gitbook.io/glint)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.gts` | [hello.gts](hello.gts) sintassi verificata |
