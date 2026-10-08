# #761 WGSL

Voce canonica `WGSL`, tipo `programming`, language_id `836605993`.

Shader compute WGSL originale che scrive i 13 codici ASCII di `Hello, World!` in un buffer storage. L’esito completo richiede un dispatch GPU e la lettura del buffer.

## Toolchain e riproduzione

naga 27.0.3 / official Rust — rustc 1.90.0 (1159e78c4 2025-09-14). Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Rust 1.90.0; il manifest fissa Naga 27.0.3 con feature `wgsl-in`. Conservare CARGO_HOME e CARGO_TARGET_DIR in una directory di lavoro esterna all’esempio. Cargo.lock registra le dipendenze risolte.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
cargo run --locked --manifest-path Cargo.toml -- hello.wgsl
```

Risultato atteso: Parser e validator accettano il modulo; in esecuzione GPU il buffer deve contenere i codici di Hello, World!.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **in attesa**.

Naga esegue parsing WGSL e validazione del modulo; il driver controlla entry point e workgroup. Queste prove attestano la sintassi e le regole statiche del modulo. Il buffer non è stato eseguito o letto da una GPU: semantica ancora in attesa.

Requisiti residui:

- GPU compatibile ed esecuzione con lettura del buffer WGSL non disponibili.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.w3.org/TR/WGSL/](https://www.w3.org/TR/WGSL/)
- [https://github.com/gfx-rs/wgpu/tree/trunk/naga](https://github.com/gfx-rs/wgpu/tree/trunk/naga)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.wgsl` | [hello.wgsl](hello.wgsl) sintassi verificata |
