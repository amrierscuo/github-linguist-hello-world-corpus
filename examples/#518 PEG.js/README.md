# #518 PEG.js

Generare un parser da una grammatica PEG.js e riconoscere il saluto.

Tipo canonico `programming`, language_id `81442128`.

Toolchain prevista: Node.js e Peggy.

Dalla cartella dell’esempio:

```sh
node verify.cjs
```

Risultato atteso: saluto riconosciuto, input errato rifiutato.

Peggy è il successore compatibile PEG.js; il parser viene generato dalla grammatica originale.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Node.js 22.20.0 + Peggy. [Log](verification/result.json). 

Fonti:

- [Peggy documentation](https://peggyjs.org/documentation.html)

Preparazione delle dipendenze in una cartella dedicata:

```sh
npm install peggy
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pegjs` | [hello.pegjs](hello.pegjs) verificato |
| `.peggy` | [hello.peggy](variants/peggy-64f146b5/hello.peggy) creato, verifiche pendenti |
