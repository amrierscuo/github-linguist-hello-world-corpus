# 0749: Verilog: `.veo`

Verilog instance template to be included in the caller.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.veo`.

Control provided, from the folder of the variant:

```text
iverilog -I . -s main -o work/hello.vvp main.v hello.v; vvp work/hello.vvp
```

Expected result: Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://docs.amd.com/r/en-US/ug901-vivado-synthesis/Instantiating-Verilog-Modules](https://docs.amd.com/r/en-US/ug901-vivado-synthesis/Instantiating-Verilog-Modules)
