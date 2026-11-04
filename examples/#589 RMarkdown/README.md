# #589 RMarkdown

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
| `.qmd` | [hello.qmd](variants/qmd-6ffe4344/hello.qmd) created; verification pending |
| `.rmd` | [hello.rmd](hello.rmd) created; verification pending |
