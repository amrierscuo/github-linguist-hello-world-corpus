# 0588: REXX: `.pprx`

## Latest recorded verification

**Syntax and behavior verified** for `.pprx`. Regina REXX parsed and executed the exact suffix variant, printing exactly Hello, World! plus LF without stderr. [Recorded evidence](../../verification/native_20261105_batch_2e70707278.json).

Textual variation of the same format, with canon suffix .pprx.

Origin: copy of the original `examples/#588 REXX/hello.rexx` file.

Artefatto principale: `hello.pprx`.

Control provided, from the folder of the variant:

```text
regina hello.pprx
```

Expected result: stdout Hello, World! and newline..

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://regina-rexx.sourceforge.io/](https://regina-rexx.sourceforge.io/)
