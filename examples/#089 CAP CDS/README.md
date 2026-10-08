# #089 CAP CDS

Definire in CAP CDS un'entità Greeting con campo message di tipo String(13), valore default Hello, World! e annotazione greeting uguale al saluto; compilare CSN e SQL.

## Toolchain

Node.js v22.20.0; @sap/cds-compiler 7.1.1

## Comandi e procedura

Da questa cartella:

```sh
npm install
node check.cjs
```

Il checker usa compileSync del compilatore SAP, legge il CSN tipizzato
ottenuto e genera SQL SQLite con compiler.to.sql. Verifica nome dell'entità,
tipo/lunghezza/default del campo e annotazione, poi il default nella SQL.

## Risultato atteso

Compilatore exit 0; CSN risolve cds.String, length=13, default.val=Hello, World!; SQL SQLite contiene DEFAULT 'Hello, World!'.

## Stato

Sintassi e semantica verificate.

La semantica verificata è quella del modello compilato e della generazione SQL. Non viene dichiarato un deployment CAP né l'esecuzione di un database.

Verifica effettiva del 2026-10-08T11:33:47.627864+00:00 su Windows x64: [log](verification/result.json).
Il log include hash SHA-256 della sorgente e dei checker, versioni, comandi, codici di uscita, stdout, stderr e limiti della prova.

## Fonti primarie

- [https://cap.cloud.sap/docs/cds/cdl](https://cap.cloud.sap/docs/cds/cdl)
- [https://cap.cloud.sap/docs/cds/csn](https://cap.cloud.sap/docs/cds/csn)
- [https://cap.cloud.sap/docs/cds/compiler/messages](https://cap.cloud.sap/docs/cds/compiler/messages)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cds` | [hello.cds](hello.cds) verificato |
