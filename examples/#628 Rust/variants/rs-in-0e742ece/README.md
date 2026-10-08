# 0628 — Rust — `.rs.in`

Variante testuale dello stesso formato, con suffisso canonico .rs.in.

Provenienza: copia del file originale `examples/#628 Rust/hello.rs`.

Artefatto principale: `hello.rs.in`.

Controllo previsto, dalla cartella della variante:

```text
rustc --crate-name greeting hello.rs.in -o work/hello
```

Risultato atteso: Hello, World! su stdout..

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://doc.rust-lang.org/book/ch01-02-hello-world.html](https://doc.rust-lang.org/book/ch01-02-hello-world.html)
