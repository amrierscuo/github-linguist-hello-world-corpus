# 0589: RMarkdown: `.qmd`

## Latest recorded verification

**Syntax and behavior verified** for `.qmd`. Quarto executed the original R code chunk and rendered an HTML output block containing exactly the greeting. Render only, with no preview or browser. [Recorded evidence](../../verification/native_20261104_followup_2e716d64.json).

Document Fourth with cell R, distinct from the frontend RMarkdown.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.qmd`.

Control provided, from the folder of the variant:

```text
quarto render hello.qmd --output-dir work
```

Expected result: HTML with Hello, World! output.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://quarto.org/docs/computations/r.html](https://quarto.org/docs/computations/r.html)
