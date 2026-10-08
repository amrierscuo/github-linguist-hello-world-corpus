# #615 Rhai

Voce canonica `Rhai`, tipo `programming`, language_id `713228814`.

Compilare un AST Rhai e catturare la stringa realmente emessa da print.

## Toolchain e riproduzione

Authentic Rhai Engine in original Rust/Cargo toolchain — Rhai 1.26.1; cargo 1.90.0 (840b83a10 2025-07-30). Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Rhai 1.26.1 autentico e Rust/Cargo 1.90.0 ufficiale. Host Rust originale e Cargo.lock garantiscono dipendenze riproducibili; target e cache sono solo work.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
cargo run --locked --quiet -- hello.rhai
```

Risultato atteso: Hello, World! nell’output o nel dato conforme, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Engine.compile_file legge lo script, eval_ast lo esegue, callback on_print raccoglie il risultato e lo confronta esattamente. Nessun interprete sostitutivo.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://rhai.rs/book/engine/hello-world.html](https://rhai.rs/book/engine/hello-world.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.rhai` | [hello.rhai](hello.rhai) verificato |
