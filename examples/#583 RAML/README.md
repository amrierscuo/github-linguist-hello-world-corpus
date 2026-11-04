# #583 RAML

Validate a RAML contract with text/plain response and an example of greeting.

Canonical type `markup`, language_id `308`.

Suggested toolchain: Node.js and raml- 1-parser.

From the example directory:

```sh
node verify.cjs
```

Expected result: no RAML error and example answer equal to greeting.

The contract does not start a service; the value is read through the parser RAML.

Recorded status: syntax verified; behavior verified. Toolchain: Node.js 22.20.0 + raml-1-parser. [Log](verification/result.json).

Sources:

- [RAML specification](https://github.com/raml-org/raml-spec/blob/master/versions/raml-10/raml-10.md)
- [RAML parser](https://github.com/raml-org/raml-js-parser-2)

Install the dependencies in a separate directory:

```sh
npm install raml-1-parser
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.raml` | [hello.raml](hello.raml) verified |
