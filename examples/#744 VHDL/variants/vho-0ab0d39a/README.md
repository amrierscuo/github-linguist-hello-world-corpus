# 0744: VHDL: `.vho`

Netlist VHDL strutturale scritta a mano con wire/constant cell originali; non dichiarata come export Quartus.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.vho`.

Control provided, from the folder of the variant:

```text
ghdl: analyze hello.vho and testbench.vhdl in work, elaborate/test greeting_tb
```

Expected result: reports notes Hello, World! after assertion on the signal.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://ghdl.github.io/ghdl/using/InvokingGHDL.html](https://ghdl.github.io/ghdl/using/InvokingGHDL.html)
