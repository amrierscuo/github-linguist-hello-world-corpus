# #588 REXX

## Latest recorded verification

Latest extension checks:
- `.pprx`: Regina REXX parsed and executed the exact suffix variant, printing exactly Hello, World! plus LF without stderr. [Evidence](verification/native_20261105_batch_2e70707278.json).
- `.rex`: Regina REXX parsed and executed the exact suffix variant, printing exactly Hello, World! plus LF without stderr. [Evidence](verification/native_20261105_batch_2e726578.json).

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
| `.pprx` | [hello.pprx](variants/pprx-57f86225/hello.pprx) syntax and behavior verified |
| `.rex` | [hello.rex](variants/rex-31adbc05/hello.rex) syntax and behavior verified |