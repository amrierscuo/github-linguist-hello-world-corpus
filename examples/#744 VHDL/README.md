# #744 VHDL

Simulate VHDL and produce a report known with greeting.

Canonical type `programming`, language_id `385`.

Suggested toolchain: GHDL 4.1.0 (Ubuntu 4.1.0+dfsg-0ubuntu2.1) [Dunoon edition]; mcode JIT backend; GNAT13.3.0; WSL Ubuntu24.04.

From the example directory:

```sh
mkdir -p build
ghdl -a --std=08 --workdir=build hello.vhdl
ghdl -e --std=08 --workdir=build hello
ghdl -r --std=08 --workdir=build hello --stop-time=1ns
```

Expected result: analisi/elaborazione successful; reports notes Hello, World!.

The string appears in the simulator report; it is not a hardware UART console.

Recorded status: syntax verified; behavior verified. Toolchain: GHDL 4.1.0 (Ubuntu 4.1.0+dfsg-0ubuntu2.1) [Dunoon edition]; mcode JIT backend; GNAT13.3.0; WSL Ubuntu24.04. [Log](verification/result.json).

Sources:

- [GHDL simulation](https://ghdl.github.io/ghdl/using/InvokingGHDL.html)

The real verification uses original Ubuntu packages extracted under `work/tools_741_760/ubuntu` and build directories separated under `work/tools_741_760`; compiled artifacts are not part of the corpus.

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.vhdl` | [hello.vhdl](hello.vhdl), [greeting.vhdl](variants/vhi-77848f30/greeting.vhdl), [main.vhdl](variants/vhi-77848f30/main.vhdl), [testbench.vhdl](variants/vho-0ab0d39a/testbench.vhdl) created; verification pending |
| `.vhd` | [hello.vhd](variants/vhd-b8ea5231/hello.vhd) created; verification pending |
| `.vhf` | [hello.vhf](variants/vhf-90e3bf30/hello.vhf) created; verification pending |
| `.vhi` | [hello.vhi](variants/vhi-77848f30/hello.vhi) created; verification pending |
| `.vho` | [hello.vho](variants/vho-0ab0d39a/hello.vho) created; verification pending |
| `.vhs` | [hello.vhs](variants/vhs-dc5efabf/hello.vhs) created; verification pending |
| `.vht` | [hello.vht](variants/vht-b9b9d435/hello.vht) created; verification pending |
| `.vhw` | [hello.vhw](variants/vhw-27e673c9/hello.vhw) created; verification pending |
