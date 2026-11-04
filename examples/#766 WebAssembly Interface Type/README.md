# #766 WebAssembly Interface Type

Voce canonica `WebAssembly Interface Type`, tipo `data`, language_id `134534086`.

Original WebAssembly WIT interface: the package corpus:greeting defines greeter.greet (string) -> string and the world greeting export the interface.

## Toolchain and reproduction

wit-parser 0.240.0 / official Rust, rustc 1.90.0 ( 1159e78c4 2025-09-14 ). Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Rust 1.90.0 and crate official wit-parser 0.240.0, fixed in the poster. Use CARGO_HOME and CARGO_TARGET_DIR external to the example; Cargo.lock retains the resolution.

Comando/procedura from the directory of the example, unless explicit indications:

```text
cargo run --locked --manifest-path Cargo.toml -- hello.wit
```

Expected result: PASS for parsing and WIT resolution; a future component will have to implement the greet method to produce greetings.

## Status and evidence

Artifact **created**; syntax **verified**; behavioral verification **pending**.

The official parser solves package, interfaces and world. The assertions control namespace and world name. WIT describes a contract: it does not contain an executable body and does not invent an implementation that stamps greeting. behavior of the waiting component.

Remaining requirements:

- Component deployment and runtime Component Model absent: verified only the interface.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://github.com/WebAssembly/component-model/blob/main/design/mvp/WIT.md](https://github.com/WebAssembly/component-model/blob/main/design/mvp/WIT.md)
- [https://github.com/bytecodealliance/wasm-tools](https://github.com/bytecodealliance/wasm-tools)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.wit` | [hello.wit](hello.wit) syntax verified |
