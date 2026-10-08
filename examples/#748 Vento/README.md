# #748 Vento

Renderizzare Vento con un valore target.

Tipo canonico `markup`, language_id `757053899`.

Toolchain prevista: Node.js22.20.0 + Vento2.4.1.

Dalla cartella dell’esempio:

```sh
node verify.cjs
```

Risultato atteso: template produce Hello, World! e newline.

Le doppie graffe vengono elaborate dal motore originale.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Node.js22 + Vento original template engine. [Log](verification/result.json). 

Fonti:

- [Vento](https://vento.js.org/)
- [Vento source](https://github.com/ventojs/vento)

Preparazione delle dipendenze in una cartella dedicata:

```sh
npm install ventojs
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.vto` | [hello.vto](hello.vto) verificato |
