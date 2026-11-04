# 0709: Tcl: `.tcl.in`

Static Tcl template without placeholder: its text remains valid Tcl.

Origin: copy of the original `examples/#709 Tcl/hello.tcl` file.

Artefatto principale: `hello.tcl.in`.

Control provided, from the folder of the variant:

```text
tclsh hello.tcl.in
```

Expected result: Hello, World! on stdout..

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.tcl-lang.org/man/tcl8.6/TclCmd/puts.htm](https://www.tcl-lang.org/man/tcl8.6/TclCmd/puts.htm)
