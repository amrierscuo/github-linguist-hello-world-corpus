# #588 REXX

Run REXX and print your greeting.

Canonical type `programming`, language_id `311`.

Suggested toolchain: Regina REXX.

From the example directory:

```sh
regina hello.rexx
```

Expected result: stdout Hello, World! and newline.

Say is a standard REXX instruction.

Recorded status: syntax verified; behavior verified. Toolchain: Regina REXX 3.9.5 native Ubuntu. [Log](verification/result.json).

Sources:

- [Regina](https://regina-rexx.sourceforge.io/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.rexx` | [hello.rexx](hello.rexx) verified |
| `.pprx` | [hello.pprx](variants/pprx-57f86225/hello.pprx) created; verification pending |
| `.rex` | [hello.rex](variants/rex-31adbc05/hello.rex) created; verification pending |
