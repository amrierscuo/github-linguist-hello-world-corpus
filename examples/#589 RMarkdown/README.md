# #589 RMarkdown

## Latest recorded verification

**Syntax and behavior verified** on November 4, 2026.

The original R Markdown chunk executed with knitr; Pandoc rendered HTML containing the greeting in the chunk output. The Quarto variant is tracked separately.

[Native commands, versions, outputs and SHA-256](verification/native_20261104_followup_main.json).

## Extension results

- `.rmd`: syntax and behavior verified.
- `.qmd`: syntax and behavior verified. [Evidence](verification/native_20261104_followup_2e716d64.json).

<details>
<summary>Original instructions and earlier status</summary>

Run a chunk R Markdown and make greetings in HTML.

Canonical type `prose`, language_id `313`.

Arranged toolchain: R, rmarkdown, knitr and Pandoc.

From the example directory:

```sh
Rscript -e "rmarkdown::render('hello.rmd')"
```

Expected result: HTML document with greeting produced by chunk R.

A Markdown parser alone does not prove the performance of the chunk.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [R Markdown](https://rmarkdown.rstudio.com/lesson-1.html)
- [knitr](https://yihui.org/knitr/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.qmd` | [hello.qmd](variants/qmd-6ffe4344/hello.qmd) syntax and behavior verified |
| `.rmd` | [hello.rmd](hello.rmd) syntax and behavior verified |

</details>
