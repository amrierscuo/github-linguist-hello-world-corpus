# 0695: SystemVerilog: `.svh`

Header SystemVerilog con macro e guard.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.svh`.

Control provided, from the folder of the variant:

```text
iverilog -g2012 -I . -o work/hello.vvp main.sv; vvp work/hello.vvp
```

Expected result: Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://steveicarus.github.io/iverilog/usage/command_line_flags.html](https://steveicarus.github.io/iverilog/usage/command_line_flags.html)
