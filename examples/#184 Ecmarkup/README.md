# #184 Ecmarkup

Compilare un documento Ecmarkup con una clausola numerata che contiene Hello, World!.

Tipo canonico `markup`, language_id `844766630`.

Toolchain prevista: Node.js 22 e ecmarkup 23.x.

Dalla cartella dell’esempio:

```sh
ecmarkup hello.html build/hello.html
```

Risultato atteso: documento HTML finale contenente la clausola sec-greeting e il paragrafo Hello, World!.

È una specifica minima in markup, senza algoritmi o affermazioni su ECMAScript. Il controllo richiede Ecmarkup, non solo un generico parser HTML.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Node.js 22.20.0 + ecmarkup 23.0.2. Vedere [log](verification/verification.log). 

Fonti del linguaggio/formato e implementazioni originali:

- [Ecmarkup — progetto TC39](https://github.com/tc39/ecmarkup)

Preparazione delle dipendenze in una cartella dedicata:

```sh
npm install --ignore-scripts --no-audit --no-fund ecmarkup@23.0.2
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.html` | [hello.html](hello.html) verificato |
