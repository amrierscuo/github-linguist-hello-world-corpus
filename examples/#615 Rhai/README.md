# #615 Rhai

Voce canonica `Rhai`, tipo `programming`, language_id `713228814`.

Fill out a AST Rhai and capture the string really issued by print.

## Toolchain and reproduction

Authentic Rhai Engine in original Rust/Cargo toolchain — Rhai 1.26.1; cargo 1.90.0 (840b83a10 2025-07-30). Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Authentic Rhai 1.26.1 and Rust/Cargo 1.90.0 official. Original Rust Host and Cargo.lock ensure reproducible dependencies; targets and caches are only work.

Comando/procedura from the directory of the example, unless explicit indications:

```text
cargo run --locked --quiet -- hello.rhai
```

Expected result: Hello, World! in output or compliant data, according to the scope described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Engine.compile_file legge lo script, eval_ast lo esegue, callback on_print raccoglie il risultato e lo confronta esattamente. Nessun interprete sostitutivo.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://rhai.rs/book/engine/hello-world.html](https://rhai.rs/book/engine/hello-world.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.rhai` | [hello.rhai](hello.rhai) verified |
