# #590 RON

Deserializzare Rusty Object Notation in una struct Rust e leggere greeting.

Tipo canonico `data`, language_id `587855233`.

Toolchain prevista: Rust Cargo, ron e serde.

Dalla cartella dell’esempio:

```sh
cargo run --quiet
```

Risultato atteso: struct con stringa Hello, World! e stdout saluto.

È il formato Rusty Object Notation di ron-rs, distinto da Replicated Object Notation.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Rust/Cargo 1.90.0 native official components + ron 0.12 + serde 1. [Log](verification/result.json). 

Fonti:

- [RON Rusty Object Notation](https://github.com/ron-rs/ron)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ron` | [hello.ron](hello.ron) verificato |
