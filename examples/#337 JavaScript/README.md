# #337 JavaScript

Eseguire JavaScript e stampare Hello, World!.

Tipo canonico `programming`, language_id `183`.

Toolchain prevista: Node.js 22.

Dalla cartella dell’esempio:

```sh
node hello.js
```

Risultato atteso: stdout Hello, World! e LF, uscita 0.

Programma JavaScript senza dipendenze.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Node.js 22.20.0. [Log](verification/result.json). 

Fonti:

- [Node.js — console.log](https://nodejs.org/api/console.html#consolelogdata-args)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.js` | [hello.js](hello.js) verificato |
| `._js` | [hello._js](variants/js-33527562/hello._js) verificato |
| `.bones` | [hello.bones](variants/bones-f53798f7/hello.bones) verificato |
| `.cjs` | [hello.cjs](variants/cjs-a7289b26/hello.cjs) verificato |
| `.es` | [hello.es](variants/es-da1cc7e7/hello.es) verificato |
| `.es6` | [hello.es6](variants/es6-0c68ffde/hello.es6) verificato |
| `.frag` | [hello.frag](variants/frag-a01c21f5/hello.frag) verificato |
| `.gs` | [hello.gs](variants/gs-86f739d3/hello.gs) creato, verifiche pendenti |
| `.jake` | [hello.jake](variants/jake-0bcd3854/hello.jake) creato, verifiche pendenti |
| `.javascript` | [hello.javascript](variants/javascript-acb7685c/hello.javascript) verificato |
| `.jsb` | [hello.jsb](variants/jsb-970d48f6/hello.jsb) verificato |
| `.jscad` | [hello.jscad](variants/jscad-b31d8173/hello.jscad) creato, verifiche pendenti |
| `.jsfl` | [hello.jsfl](variants/jsfl-8b8ff6e5/hello.jsfl) creato, verifiche pendenti |
| `.jslib` | [hello.jslib](variants/jslib-3de44ffa/hello.jslib) verificato |
| `.jsm` | [hello.jsm](variants/jsm-b354178f/hello.jsm) creato, verifiche pendenti |
| `.jspre` | [hello.jspre](variants/jspre-80d28e27/hello.jspre) verificato |
| `.jss` | [hello.jss](variants/jss-a28ab28f/hello.jss) verificato |
| `.jsx` | [hello.jsx](variants/jsx-9285fe67/hello.jsx) creato, verifiche pendenti |
| `.mjs` | [hello.mjs](variants/mjs-c0d5ab99/hello.mjs) verificato |
| `.njs` | [hello.njs](variants/njs-c96809ca/hello.njs) creato, verifiche pendenti |
| `.pac` | [hello.pac](variants/pac-2217726f/hello.pac) creato, verifiche pendenti |
| `.sjs` | [hello.sjs](variants/sjs-9d6365fe/hello.sjs) creato, verifiche pendenti |
| `.ssjs` | [hello.ssjs](variants/ssjs-7ae3cfef/hello.ssjs) creato, verifiche pendenti |
| `.xsjs` | [hello.xsjs](variants/xsjs-a22c7604/hello.xsjs) creato, verifiche pendenti |
| `.xsjslib` | [hello.xsjslib](variants/xsjslib-3de3922e/hello.xsjslib) creato, verifiche pendenti |
