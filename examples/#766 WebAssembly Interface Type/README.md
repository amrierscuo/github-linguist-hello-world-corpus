# #766 WebAssembly Interface Type

Voce canonica `WebAssembly Interface Type`, tipo `data`, language_id `134534086`.

Interfaccia WebAssembly WIT originale: il package corpus:greeting definisce greeter.greet(string) -> string e il world greeting ne esporta l’interfaccia.

## Toolchain e riproduzione

wit-parser 0.240.0 / official Rust — rustc 1.90.0 (1159e78c4 2025-09-14). Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Rust 1.90.0 e crate ufficiale wit-parser 0.240.0, fissato nel manifest. Usare CARGO_HOME e CARGO_TARGET_DIR esterni all’esempio; Cargo.lock conserva la risoluzione.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
cargo run --locked --manifest-path Cargo.toml -- hello.wit
```

Risultato atteso: PASS per parsing e risoluzione WIT; un futuro componente dovrà implementare il metodo greet per produrre il saluto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **in attesa**.

Il parser ufficiale risolve package, interfacce e world. Le asserzioni controllano namespace e nome del world. WIT descrive un contratto: non contiene un corpo eseguibile e non viene inventata una implementazione che stampi il saluto. Semantica del componente in attesa.

Requisiti residui:

- Implementazione del componente e runtime Component Model assenti: verificata soltanto l’interfaccia.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://github.com/WebAssembly/component-model/blob/main/design/mvp/WIT.md](https://github.com/WebAssembly/component-model/blob/main/design/mvp/WIT.md)
- [https://github.com/bytecodealliance/wasm-tools](https://github.com/bytecodealliance/wasm-tools)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.wit` | [hello.wit](hello.wit) sintassi verificata |
