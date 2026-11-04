# 0582: R: `.rd`

## Recorded verification

**Syntax and behavior verified** on November 4, 2026. Run the original Rd markup through the native R help formatter and assert that the produced help text contains the greeting. [Evidence](../../verification/native_20261104_582_variants_result.json).

Rd help document, not R script.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.rd`.

Control provided, from the folder of the variant:

```text
R CMD Rd2txt hello.rd > work/greeting.txt
```

Expected result: help document with title Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://cran.r-project.org/doc/manuals/r-release/R-exts.html#Rd-format](https://cran.r-project.org/doc/manuals/r-release/R-exts.html#Rd-format)
