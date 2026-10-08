# #583 RAML

Validare un contratto RAML con risposta text/plain ed esempio di saluto.

Tipo canonico `markup`, language_id `308`.

Toolchain prevista: Node.js e raml-1-parser.

Dalla cartella dell’esempio:

```sh
node verify.cjs
```

Risultato atteso: nessun errore RAML e risposta example uguale al saluto.

Il contratto non avvia un servizio; il valore è letto attraverso il parser RAML.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Node.js 22.20.0 + raml-1-parser. [Log](verification/result.json). 

Fonti:

- [RAML specification](https://github.com/raml-org/raml-spec/blob/master/versions/raml-10/raml-10.md)
- [RAML parser](https://github.com/raml-org/raml-js-parser-2)

Preparazione delle dipendenze in una cartella dedicata:

```sh
npm install raml-1-parser
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.raml` | [hello.raml](hello.raml) verificato |
