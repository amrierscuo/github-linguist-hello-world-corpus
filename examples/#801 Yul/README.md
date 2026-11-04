# #801 Yul

Voce e ordine canonici di `reference/languages.yml`.

Fill out the original source and return `Hello, World!` by using the bytecode in a local virtual machine.

## Toolchain and reproduction

Solc 0.8.37 + EthereumJS EVM 10.1.3; Node.js 22.20.0. Run from the example folder:

```sh
npm install --no-audit --no-fund --save-exact solc@0.8.37 @ethereumjs/evm@10.1.3
node verify.cjs
```

The checker performs bytecodes produced by solc with EthereumJS EVM, hardfork Prague. Check absence of exceptions and all 13 byte returned by RETURN.

Verification only uses a local VM and does not require accounts, funds or connection to a blockchain.

## State and Test

syntax and behavior verified `2026-10-08T23:31:22.707883+00:00`. Real result: `Hello, World!`.

[Log della verifica](verification/runtime.json) with versions, commands, stdout, exit code and SHA-256 of sources and checker.

## Primary sources

- [https://docs.soliditylang.org/en/latest/yul.html](https://docs.soliditylang.org/en/latest/yul.html)
- [https://github.com/ethereumjs/ethereumjs-monorepo/tree/master/packages/evm](https://github.com/ethereumjs/ethereumjs-monorepo/tree/master/packages/evm)

## Extension coverage

Suffix checks are recorded separately.

| Extension | File and status |
| --- | --- |
| `.yul` | [hello.yul](hello.yul) syntax and behavior verified |
