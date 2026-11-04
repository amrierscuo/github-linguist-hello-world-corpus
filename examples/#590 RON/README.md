# #590 RON

Deserialize Rusty Object Notation in a struct Rust and read greeting.

Canonical type `data`, language_id `587855233`.

Suggested toolchain: Rust Cargo, ron and serde.

From the example directory:

```sh
cargo run --quiet
```

Expected result: struct with Hello, World! string and stdout greeting.

It is the Rusty Object Notation format of ron-rs, distinguished by Replicated Object Notation.

Recorded status: syntax verified; behavior verified. Toolchain: Rust/Cargo 1.90.0 native official components + ron 0.12 + serde 1. [Log](verification/result.json).

Sources:

- [RON Rusty Object Notation](https://github.com/ron-rs/ron)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ron` | [hello.ron](hello.ron) verified |
