# 0623: Roff: `.nr`

Source nroff/troff textual; no conversion to RUNOFF DEC is declared.

Origin: copy of the original `examples/#623 Roff/hello.roff` file.

Artefatto principale: `hello.nr`.

Control provided, from the folder of the variant:

```text
groff -Tascii hello.nr
```

Expected result: Text output contains Hello, World!..

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.gnu.org/software/groff/manual/groff.html](https://www.gnu.org/software/groff/manual/groff.html)
