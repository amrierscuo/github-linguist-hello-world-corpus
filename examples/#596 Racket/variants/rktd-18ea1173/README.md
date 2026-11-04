# 0596: Racket: `.rktd`

## Recorded verification

**Syntax and behavior verified** on November 4, 2026. Load the literal hash through the Racket reader, run the loadable file via the original evaluator, and render Scribble to HTML; assert the greeting in each output. [Evidence](../../verification/native_20261104_596_variants_result.json).

Datum Racket serializable: hash that keeps greeting.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.rktd`.

Control provided, from the folder of the variant:

```text
racket -e '(displayln (hash-ref (call-with-input-file "hello.rktd" read) (quote greeting)))'
```

Expected result: Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://docs.racket-lang.org/reference/reader.html](https://docs.racket-lang.org/reference/reader.html)
