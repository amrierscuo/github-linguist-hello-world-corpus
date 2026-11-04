# 0709: Tcl: `.sdc`

Constraint Tcl for Synopsys SDC timing; requires a design with clk port.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.sdc`.

Control provided, from the folder of the variant:

```text
native FPGA/STA tool: load RTL main.v and read SDC hello.sdc
```

Expected result: clock corpus_greeting with period 10 ns; RTL simulation produces Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://docs.amd.com/r/en-US/ug903-vivado-using-constraints/Clock-Definition](https://docs.amd.com/r/en-US/ug903-vivado-using-constraints/Clock-Definition)
