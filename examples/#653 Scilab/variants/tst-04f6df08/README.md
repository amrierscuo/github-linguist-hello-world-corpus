# 0653: Scilab: `.tst`

## Latest recorded verification

**Syntax and behavior verified** for `.tst`. The minimal native Scilab command-line interpreter ran the original .sce script; separately loaded and called the original .sci function through its original companion driver; and executed the .tst assertion. Each emitted the exact greeting. The nwni mode uses GUI/graphics/JVM-disabled libraries, with no display supplied and no GUI library linkage. [Recorded evidence](../../verification/native_20261105_batch_main.json).

Test Scilab con assertion reale.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.tst`.

Control provided, from the folder of the variant:

```text
scilab-cli -nb -f hello.tst
```

Expected result: assertion passes and Hello, World! console.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://help.scilab.org/docs/2025.1.0/en_US/assert_checkequal.html](https://help.scilab.org/docs/2025.1.0/en_US/assert_checkequal.html)
