# #111 CartoCSS

Fill out a CartoCSS style in a TextSymbolizer Mapnik containing the Hello, World! label.

Canonical type: `programming`; `language_id`: `53`.

Suggested toolchain: Node.js 22 and 1.2.0 cart. The version actually tried, when available, is in the log.

From the example folder, depending on the PATH:

```sh
node verify.cjs
```

Expected result: XML Mapnik accepted by the CartoCSS compiler with TextSymbolizer, greeting and expected fonts.

The control concerns the translation of the style in XML and the presence of the text; rendering of a map and the actual availability of the font in Mapnik are additional verifications.

Recorded status: syntax verified; behavior verified. Tried toolchain: Node.js 22.20.0 + 1.2.0 cart. See [log](verification/verification.log).

Primary sources or original references of the project:

- [CartoCSS — implementazione originale](https://github.com/mapbox/carto)
- [CARTO — proprietà del testo](https://cartodb.github.io/developers/styling/cartocss/)

Reproducible dependencies in a dedicated workbook:

```sh
npm install --ignore-scripts --no-audit --no-fund carto@1.2.0
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mss` | [hello.mss](hello.mss) verified |
