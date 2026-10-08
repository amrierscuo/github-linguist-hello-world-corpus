# #628 Rust

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Compilare Rust e stampare Hello, World!.

Programma nativo compilato con rustc ufficiale; interpolazione della variabile audience in println!. Nessun crate esterno.

## Toolchain e riproduzione

Rustc1.90.0 ufficiale

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
rustc hello.rs -o hello && ./hello
```

## Risultato atteso e stato

Hello, World! su stdout.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://doc.rust-lang.org/book/ch01-02-hello-world.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.rs` | [hello.rs](hello.rs) verificato |
| `.rs.in` | [hello.rs.in](variants/rs-in-0e742ece/hello.rs.in) creato, verifiche pendenti |
