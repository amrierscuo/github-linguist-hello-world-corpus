# #749 Verilog

Simulate a Verilog module that performs display and finish.

Canonical type `programming`, language_id `387`.

Suggested toolchain: Icarus Verilog12.0 native Linux compiler/vvp.

From the example directory:

```sh
iverilog -o build/hello.vvp hello.v
vvp build/hello.vvp
```

Expected result: The simulation prints a Hello, World! line and the normal diagnostic $finish called at 0; exit0.

The program does not describe an external device: it is a simulation testbench.

Recorded status: syntax verified; behavior verified. Toolchain: Icarus Verilog12.0 original compiler/vvp native Linux. [Log](verification/result.json).

Sources:

- [Icarus Verilog](https://steveicarus.github.io/iverilog/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.v` | [hello.v](hello.v), [hello.v](variants/veo-6cbf9bdf/hello.v), [main.v](variants/veo-6cbf9bdf/main.v) created; verification pending |
| `.veo` | [hello.veo](variants/veo-6cbf9bdf/hello.veo) created; verification pending |
