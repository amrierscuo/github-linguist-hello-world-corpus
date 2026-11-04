# #709 Tcl

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Eseguire Tcl e stampare Hello, World!.

Interpolation of the variable audience and puts of the authentic Tcl runtime.

## Toolchain and reproduction

Tcl8.6 original, Ubuntu version in the log

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
tclsh hello.tcl
```

## Expected result and status

Hello, World! su stdout.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://www.tcl-lang.org/man/tcl8.6/TclCmd/puts.htm

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.tcl` | [hello.tcl](hello.tcl), [main.tcl](variants/tm-cb765f5d/main.tcl) created; verification pending |
| `.adp` | [hello.adp](variants/adp-fdf7bf5a/hello.adp) created; verification pending |
| `.sdc` | [hello.sdc](variants/sdc-c14a8049/hello.sdc) created; verification pending |
| `.tcl.in` | [hello.tcl.in](variants/tcl-in-4fd82009/hello.tcl.in) created; verification pending |
| `.tm` | [corpus-greeting-0.1.tm](variants/tm-cb765f5d/corpus-greeting-0.1.tm) created; verification pending |
| `.xdc` | [hello.xdc](variants/xdc-305793a9/hello.xdc) created; verification pending |
