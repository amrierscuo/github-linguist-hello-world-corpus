# 0744: VHDL: `.vhw`

Textual variation of the same format, with canon suffix .vhw.

Origin: copy of the original `examples/#744 VHDL/hello.vhdl` file.

Artefatto principale: `hello.vhw`.

Control provided, from the folder of the variant:

```text
ghdl -a --std=08 --workdir=work hello.vhw
ghdl -e --std=08 --workdir=work hello
ghdl -r --std=08 --workdir=work hello --stop-time=1ns
```

Expected result: analisi/elaborazione successful; reports notes Hello, World!..

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://ghdl.github.io/ghdl/using/InvokingGHDL.html](https://ghdl.github.io/ghdl/using/InvokingGHDL.html)
