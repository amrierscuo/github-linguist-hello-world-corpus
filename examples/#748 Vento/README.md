# #748 Vento

Render Wind with a target value.

Canonical type `markup`, language_id `757053899`.

Suggested toolchain: Node.js22.20.0 + Vento2.4.1.

From the example directory:

```sh
node verify.cjs
```

Expected result: template produces Hello, World! and newline.

The double scratches are processed by the original engine.

Recorded status: syntax verified; behavior verified. Toolchain: Node.js22 + Vento original template engine. [Log](verification/result.json).

Sources:

- [Vento](https://vento.js.org/)
- [Vento source](https://github.com/ventojs/vento)

Install the dependencies in a separate directory:

```sh
npm install ventojs
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.vto` | [hello.vto](hello.vto) verified |
