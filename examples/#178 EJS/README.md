# #178 EJS

Compilare un template EJS e ottenere un titolo HTML Hello, World! tramite interpolation escaped.

## Toolchain

Node.js v22.20.0; ejs 7.0.1

## Comandi e procedura

npm install; node check.cjs

## Risultato atteso

HTML esattamente <h1>Hello, World!</h1> più newline; <world> viene escaped correttamente.

## Stato

Sintassi e semantica verificate.

locals.json fornisce il dato; il template usa <%= greeting %>. La prova verifica il motore EJS e l’escaping, senza pretendere una resa nel browser.

Verifica effettiva del 2026-10-08T11:56:13.767905+00:00 su Windows x64: [log](verification/result.json).
Hash delle sorgenti/checker, versioni e comandi reali, codici di uscita, stdout/stderr e limiti della prova sono nel log.

## Fonti primarie e riferimento di formato

- [https://ejs.co/#docs](https://ejs.co/#docs)
- [https://github.com/mde/ejs](https://github.com/mde/ejs)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ejs` | [hello.ejs](hello.ejs) verificato |
| `.ect` | [hello.ect](variants/ext-ect-2e656374/hello.ect) creato, verifiche pendenti |
| `.ejs.t` | [hello.ejs.t](variants/ext-ejs-t-2e656a732e74/hello.ejs.t) creato, verifiche pendenti |
| `.jst` | [hello.jst](variants/ext-jst-2e6a7374/hello.jst) creato, verifiche pendenti |
