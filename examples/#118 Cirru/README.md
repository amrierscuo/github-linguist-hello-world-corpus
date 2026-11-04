# #118 Cirru

Fill out an expression CirruScript from Cirru grammar in JavaScript and execute it to print Hello, World!.

Canonical type: `programming`; `language_id`: `58`.

Suggested toolchain: Node.js 22 and cirru-script 0.6.2 (original historical implementation).

From the example folder, depending on the PATH:

```sh
cirruscript hello.cirru
```

Expected result: stdout `Hello, World!` followed by newline.

Cirru è una grammatica utilizzabile da più linguaggi; questo esempio seleziona esplicitamente il dialetto CirruScript storico. Il parser della grammatica da solo non prova l’esecuzione del saluto.

Recorded status: syntax verified; behavior verified. Tried toolchain: Node.js 22.20.0 + cirru-script 0.6.2. See [log](verification/verification.log).

Primary sources or original references of the project:

- [CirruScript — compilatore originale](https://github.com/Cirru/cirru-script)
- [Cirru — parser originale](https://github.com/Cirru/parser.coffee)

Automatic verification included: `node verify.cjs`.

Reproducible dependencies in a dedicated workbook:

```sh
npm install --ignore-scripts --no-audit --no-fund cirru-script@0.6.2
```

In CirruScript the `:` prefix identifies a string value. The quotes protect the token spaces; the prefix is not part of the printed text.

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cirru` | [hello.cirru](hello.cirru) verified |
