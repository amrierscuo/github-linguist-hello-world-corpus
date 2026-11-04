# #184 Ecmarkup

Fill out an Ecmarkup document with a numbered clause containing Hello, World!.

Canonical type `markup`, language_id `844766630`.

Suggested toolchain: Node.js 22 and ecmarkup 23.x.

From the example directory:

```sh
ecmarkup hello.html build/hello.html
```

Expected result: final HTML document containing the sec-greeting clause and the Hello, World! paragraph.

It is a minimum markup specification, without algorithms or statements on ECMAScript. Control requires Ecmarkup, not only a generic parser HTML.

Recorded status: syntax verified; behavior verified. Toolchain: Node.js 22.20.0 + ecmarkup 23.0.2. See [log](verification/verification.log).

Sources of linguaggio/formato and original implementations:

- [Ecmarkup — progetto TC39](https://github.com/tc39/ecmarkup)

Install the dependencies in a separate directory:

```sh
npm install --ignore-scripts --no-audit --no-fund ecmarkup@23.0.2
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.html` | [hello.html](hello.html) verified |
