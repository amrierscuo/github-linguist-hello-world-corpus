# #582 R

Run R and print your greeting.

Canonical type `programming`, language_id `307`.

Suggested toolchain: GNU Rscript.

From the example directory:

```sh
Rscript --vanilla hello.r
```

Expected result: stdout Hello, World! and newline.

cat writes without prefix [ 1 ] and without quotes.

Recorded status: syntax verified; behavior verified. Toolchain: GNU R 4.3.3 native Ubuntu runtime. [Log](verification/result.json).

Sources:

- [R introduction](https://cran.r-project.org/doc/manuals/r-release/R-intro.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.r` | [hello.r](hello.r) verified |
| `.rd` | [hello.rd](variants/rd-0443eb91/hello.rd) syntax and behavior verified |
| `.rhistory` | [hello.rhistory](variants/rhistory-375f1003/hello.rhistory) created; verification pending |
| `.rsx` | [hello.rsx](variants/rsx-7f28a360/hello.rsx) created; verification pending |

## Additional extension verification

- `.rd`: verified on November 4, 2026. [Evidence](verification/native_20261104_582_variants_result.json).
