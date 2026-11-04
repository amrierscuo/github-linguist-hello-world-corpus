# 0628: Rust: `.rs.in`

Textual variation of the same format, with canon suffix .rs.in.

Origin: copy of the original `examples/#628 Rust/hello.rs` file.

Artefatto principale: `hello.rs.in`.

Control provided, from the folder of the variant:

```text
rustc --crate-name greeting hello.rs.in -o work/hello
```

Expected result: Hello, World! on stdout..

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://doc.rust-lang.org/book/ch01-02-hello-world.html](https://doc.rust-lang.org/book/ch01-02-hello-world.html)
