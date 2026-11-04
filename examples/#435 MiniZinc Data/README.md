# #435 MiniZinc Data

Load separate MiniZinc data and use them in the model to build greetings.

Canonical type `data`, language_id `938193433`.

Suggested toolchain: MiniZinc CLI and solver Gecode.

From the example directory:

```sh
minizinc --solver gecode model.mzn hello.dzn
```

Expected result: accepted data; solution with Hello, World! output.

hello.dzn is the primary data artifact; model.mzn is the consumer who checks the value charged.

Recorded status: syntax verified; behavior verified. Toolchain: MiniZinc 2.10.1 official Linux bundle + Gecode. [Log](verification/result.json).

Sources:

- [MiniZinc — data files](https://docs.minizinc.dev/en/stable/modelling.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.dzn` | [hello.dzn](hello.dzn) verified |
