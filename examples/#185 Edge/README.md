# #185 Edge

Render a Edge template by replacing targets with World and get Hello, World!.

Canonical type `markup`, language_id `460509620`.

Suggested toolchain: Node.js 22 and edge.js 6.5.1.

From the example directory:

```sh
node verify.cjs
```

Expected result: exact stdout `Hello, World!\n`, 0. output

Il dato passato al renderer è locale e costante. Non viene avviato un server web.

Recorded status: syntax verified; behavior verified. Toolchain: Node.js 22.20.0 + edge.js 6.5.1. See [log](verification/verification.log).

Sources of linguaggio/formato and original implementations:

- [Edge — documentazione del motore](https://edgejs.dev/docs/introduction)
- [Edge — implementazione](https://github.com/edge-js/edge)

Install the dependencies in a separate directory:

```sh
npm install --ignore-scripts --no-audit --no-fund edge.js@6.5.1
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.edge` | [hello.edge](hello.edge) verified |
