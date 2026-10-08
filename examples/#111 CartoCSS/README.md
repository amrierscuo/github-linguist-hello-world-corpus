# #111 CartoCSS

Compilare uno stile CartoCSS in un TextSymbolizer Mapnik contenente l’etichetta Hello, World!.

Tipo canonico: `programming`; `language_id`: `53`.

Toolchain prevista: Node.js 22 e carto 1.2.0. La versione effettivamente provata, quando disponibile, è nel log.

Dalla cartella dell'esempio, con le dipendenze nel PATH:

```sh
node verify.cjs
```

Risultato atteso: XML Mapnik accettato dal compilatore CartoCSS con TextSymbolizer, saluto e font previsti.

Il controllo riguarda la traduzione dello stile in XML e la presenza del testo; il rendering di una mappa e la disponibilità effettiva del font in Mapnik sono verifiche ulteriori.

Stato registrato: sintassi verificata; semantica verificata. Toolchain provata: Node.js 22.20.0 + carto 1.2.0. Vedere [log](verification/verification.log). 

Fonti primarie o riferimenti originali del progetto:

- [CartoCSS — implementazione originale](https://github.com/mapbox/carto)
- [CARTO — proprietà del testo](https://cartodb.github.io/developers/styling/cartocss/)

Dipendenze riproducibili in una cartella di lavoro dedicata:

```sh
npm install --ignore-scripts --no-audit --no-fund carto@1.2.0
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mss` | [hello.mss](hello.mss) verificato |
