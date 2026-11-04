# #581 Quint

Check with Quint a pure expression that returns greeting.

Canonical type `programming`, language_id `562056483`.

Suggested toolchain: Quint CLI.

From the example directory:

```sh
quint typecheck hello.qnt
quint test hello.qnt
```

Expected result: successful typecheck and greetingTest passes.

Quint is a specific language: the behavior consists in evaluating the string test, without claiming I/O of console.

Recorded status: syntax verified; behavior verified. Toolchain: Node.js 22.20.0 + original Quint CLI. [Log](verification/result.json).

Sources:

- [Quint language](https://github.com/quint-co/quint/blob/main/docs/content/docs/lang.md)
- [Quint CLI](https://github.com/quint-co/quint/blob/main/docs/content/docs/quint.md)

Install the dependencies in a separate directory:

```sh
npm install @informalsystems/quint
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.qnt` | [hello.qnt](hello.qnt) verified |
