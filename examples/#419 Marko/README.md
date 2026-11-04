# #419 Marko

Fill Marko and make HTML with input.target equal to World.

Canonical type `markup`, language_id `932782397`.

Suggested toolchain: Node.js 22 and Marko 5.39.45.

From the example directory:

```sh
node verify.cjs
```

Expected result: HTML <p> Hello, World! </p> with only possible external whitespace; stdout greeting and LF.

The generated JavaScript is loaded into memory using the Marko real runtime; no compiled files included in the corpus.

Recorded status: syntax verified; behavior verified. Toolchain: Node.js 22.20.0 + Marko 5.39.45 + @marko/compiler 5.42.10 + he 1.2.0. [Log](verification/result.json).

Sources:

- [Marko — documentazione](https://markojs.com/docs/)
- [Marko — compilatore](https://github.com/marko-js/marko)

Install the dependencies in a separate directory:

```sh
npm install --ignore-scripts --no-audit --no-fund marko@5.39.45 @marko/compiler@5.42.10 he@1.2.0
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.marko` | [hello.marko](hello.marko) verified |
