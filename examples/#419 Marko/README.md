# #419 Marko

Compilare Marko e renderizzare HTML con input.target uguale a World.

Tipo canonico `markup`, language_id `932782397`.

Toolchain prevista: Node.js 22 e Marko 5.39.45.

Dalla cartella dell’esempio:

```sh
node verify.cjs
```

Risultato atteso: HTML <p>Hello, World!</p> con solo eventuale whitespace esterno; stdout saluto e LF.

Il JavaScript generato viene caricato in memoria usando il runtime Marko reale; nessun file compilato incluso nel corpus.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Node.js 22.20.0 + Marko 5.39.45 + @marko/compiler 5.42.10 + he 1.2.0. [Log](verification/result.json). 

Fonti:

- [Marko — documentazione](https://markojs.com/docs/)
- [Marko — compilatore](https://github.com/marko-js/marko)

Preparazione delle dipendenze in una cartella dedicata:

```sh
npm install --ignore-scripts --no-audit --no-fund marko@5.39.45 @marko/compiler@5.42.10 he@1.2.0
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.marko` | [hello.marko](hello.marko) verificato |
