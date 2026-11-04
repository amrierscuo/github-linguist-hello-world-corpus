# 0744: VHDL: `.vhi`

VHDL instance template to be inserted in the storage system; not autonomous VHDL drive.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.vhi`.

Control provided, from the folder of the variant:

```text
ghdl: analyze greeting.vhdl and expanded main.vhdl; simulate main
```

Expected result: signal message assumes Hello, World! and known report of the caller.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://docs.amd.com/r/en-US/ug901-vivado-synthesis/Using-VHDL-Instantiation-Templates](https://docs.amd.com/r/en-US/ug901-vivado-synthesis/Using-VHDL-Instantiation-Templates)
