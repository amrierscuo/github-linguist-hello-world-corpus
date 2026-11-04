# #628 Rust

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Fill in Rust and print Hello, World!.

Native program compiled with official rustc; interpolation of the audience variable in println!. No external waxes.

## Toolchain and reproduction

Rustc1.90.0 ufficiale

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
rustc hello.rs -o hello && ./hello
```

## Expected result and status

Hello, World! su stdout.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://doc.rust-lang.org/book/ch01-02-hello-world.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.rs` | [hello.rs](hello.rs) verified |
| `.rs.in` | [hello.rs.in](variants/rs-in-0e742ece/hello.rs.in) created; verification pending |
