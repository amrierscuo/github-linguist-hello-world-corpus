# 0653: Scilab: `.sci`

## Latest recorded verification

**Syntax and behavior verified** for `.sci`. The minimal native Scilab command-line interpreter ran the original .sce script; separately loaded and called the original .sci function through its original companion driver; and executed the .tst assertion. Each emitted the exact greeting. The nwni mode uses GUI/graphics/JVM-disabled libraries, with no display supplied and no GUI library linkage. [Recorded evidence](../../verification/native_20261105_batch_main.json).

Function Scilab files, loaded by the caller.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.sci`.

Control provided, from the folder of the variant:

```text
scilab-cli -nb -f main.sce
```

Expected result: Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://help.scilab.org/docs/2025.1.0/en_US/mprintf.html](https://help.scilab.org/docs/2025.1.0/en_US/mprintf.html)
