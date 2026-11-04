# #740 V

The original source compiles with V and `Hello, World!` print.

Canonical type `programming`, language_id `603371597`.

## Toolchain and reproduction

Test performed with official compiler V 0.5.2 (commit `7647ce1`) and GCC 13.3.0 in Ubuntu 24.04 WSL2, x86_64 architecture.

From the example folder, with an output folder already created:

```sh
v -cc gcc -o build/hello hello.v
./build/hello
```

The compilation command ends with exit code 0. The native track returns exactly `Hello, World!` followed by newline and ends with exit code 0.

## Status and evidence

syntax and behavior verified. The only presence of `.v` file does not determine this state: the V compiler has accepted the registered bytes and the track has been executed.

[Log nativo](verification/native.json) con comandi effettivi, timestamp UTC, versioni, stdout/stderr e SHA256 di sorgente, toolchain e prodotto compilato. I percorsi personali sono sostituiti da `<corpus>`, `<work>` e `<workspace>`; i byte del sorgente rimangono invariati.

## Primary sources

- [Documentazione V](https://docs.vlang.io/)
- [Release ufficiale V 0.5.2](https://github.com/vlang/v/releases/tag/0.5.2)

## Extension coverage

Each suffix maintains its own test; the pending variants do not inherit verifications.

| Extension | File and status |
| --- | --- |
| `.v` | [hello.v](hello.v) syntax and behavior verified |
