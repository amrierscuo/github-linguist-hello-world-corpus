# #706 Tact

Voce e ordine canonici di `reference/languages.yml`.

Fill out the original source and return `Hello, World!` by using the bytecode in a local virtual machine.

## Toolchain and reproduction

Tact 1.6.13 + TON Sandbox 0.45.0 + tsx 4.23.15; Node.js 22.20.0. Run from the example folder:

```sh
npm install --no-audit --no-fund --save-exact @tact-lang/compiler@1.6.13 @ton/sandbox@0.45.0 @ton/core@0.63.1 @ton/crypto@3.3.0 tsx@4.23.15
node verify.cjs
```

The checker compiles Tact in a local temporary folder. Use the StateInit of the TypeScript wrapper produced by the compiler, performs the getter greeting in the TVM and controls both the stack and the official wrapper result.

Verification only uses a local VM and does not require accounts, funds or connection to a blockchain.

## State and Test

syntax and behavior verified `2026-10-08T23:31:25.959856+00:00`. Real result: `Hello, World!`.

[Log della verifica](verification/runtime.json) with versions, commands, stdout, exit code and SHA-256 of sources and checker.

## Primary sources

- [https://docs.tact-lang.org/book/contracts/](https://docs.tact-lang.org/book/contracts/)
- [https://github.com/ton-blockchain/sandbox](https://github.com/ton-blockchain/sandbox)

## Extension coverage

Suffix checks are recorded separately.

| Extension | File and status |
| --- | --- |
| `.tact` | [hello.tact](hello.tact) syntax and behavior verified |
