# #723 Tolk

Voce e ordine canonici di `reference/languages.yml`.

Fill out the original source and return `Hello, World!` by using the bytecode in a local virtual machine.

## Toolchain and reproduction

Tolk 1.4.2 + TON Sandbox 0.45.0; Node.js 22.20.0. Run from the example folder:

```sh
npm install --no-audit --no-fund --save-exact @ton/tolk-js@1.4.2 @ton/sandbox@0.45.0 @ton/core@0.63.1 @ton/crypto@3.3.0
node verify.cjs
```

The checker compiles with Tolk and loads code and blank data cell in the TON Sandbox. Executes the getter greeting in the TVM and controls exit code 0 and returns string.

Verification only uses a local VM and does not require accounts, funds or connection to a blockchain.

## State and Test

syntax and behavior verified `2026-10-08T23:31:23.792787+00:00`. Real result: `Hello, World!`.

[Log della verifica](verification/runtime.json) with versions, commands, stdout, exit code and SHA-256 of sources and checker.

## Primary sources

- [https://docs.ton.org/tolk/overview](https://docs.ton.org/tolk/overview)
- [https://github.com/ton-blockchain/tolk-js](https://github.com/ton-blockchain/tolk-js)
- [https://github.com/ton-blockchain/sandbox](https://github.com/ton-blockchain/sandbox)

## Extension coverage

Suffix checks are recorded separately.

| Extension | File and status |
| --- | --- |
| `.tolk` | [hello.tolk](hello.tolk) syntax and behavior verified |
