# #434 MiniZinc

Solve a MiniZinc model without constraints and produce greeting in output.

Canonical type `programming`, language_id `238874535`.

Suggested toolchain: MiniZinc CLI and solver Gecode.

From the example directory:

```sh
minizinc --solver gecode hello.mzn
```

Expected result: satisfactory solution with Hello, World! line in output.

The solve item and item output are interpreted by the real MiniZinc compiler.

Recorded status: syntax verified; behavior verified. Toolchain: MiniZinc 2.10.1 official Linux bundle + Gecode. [Log](verification/result.json).

Sources:

- [MiniZinc — manuale](https://docs.minizinc.dev/en/stable/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mzn` | [hello.mzn](hello.mzn) verified |
