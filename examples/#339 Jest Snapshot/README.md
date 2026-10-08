# #339 Jest Snapshot

Leggere uno snapshot Jest originale e confrontarlo con il valore Hello, World!.

Tipo canonico `data`, language_id `774635084`.

Toolchain prevista: Node.js 22 e jest-snapshot 30.2.0.

Dalla cartella dell’esempio:

```sh
node verify.cjs
```

Risultato atteso: snapshot greeting 1 caricato e confronto riuscito; stdout saluto e LF.

updateSnapshot è none: il checker deve confrontare il file esistente e non creare o aggiornare aspettative.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Node.js 22.20.0 + jest-snapshot 30.2.0. [Log](verification/result.json). 

Fonti:

- [Jest — snapshot testing](https://jestjs.io/docs/snapshot-testing)
- [Jest — implementazione SnapshotState](https://github.com/jestjs/jest/tree/main/packages/jest-snapshot)

Preparazione delle dipendenze in una cartella dedicata:

```sh
npm install --ignore-scripts --no-audit --no-fund jest-snapshot@30.2.0
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.snap` | [greeting.test.js.snap](greeting.test.js.snap) verificato |
