# #596 Racket

Run a Racket form and print your greeting.

Canonical type `programming`, language_id `316`.

Suggested toolchain: Racket.

From the example directory:

```sh
racket hello.rkt
```

Expected result: stdout Hello, World! and newline.

Basic module without external dependencies.

Recorded status: syntax verified; behavior verified. Toolchain: Racket 8.18 native Windows portable. [Log](verification/result.json).

Sources:

- [Racket displayln](https://docs.racket-lang.org/reference/Writing.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.rkt` | [hello.rkt](hello.rkt) verified |
| `.rktd` | [hello.rktd](variants/rktd-18ea1173/hello.rktd) syntax and behavior verified |
| `.rktl` | [hello.rktl](variants/rktl-c9a39abc/hello.rktl) syntax and behavior verified |
| `.scrbl` | [hello.scrbl](variants/scrbl-ba477af2/hello.scrbl) created; verification pending |

## Additional extension verification

- `.rktd`: verified on November 4, 2026. [Evidence](verification/native_20261104_596_variants_result.json).
- `.rktl`: verified on November 4, 2026. [Evidence](verification/native_20261104_596_variants_result.json).
