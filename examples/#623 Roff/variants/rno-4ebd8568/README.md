# 0623: Roff: `.rno`

## Latest recorded verification

**Syntax and behavior verified** for `.rno`. Native groff rendered the exact variant using its plain, man, mdoc, me or ms input as recorded; the rendered text contains Hello, World!. Macro includes were loaded natively when present. No GUI renderer was used. [Recorded evidence](../../verification/native_20261105_batch_2e726e6f.json).

Source nroff/troff textual; no conversion to RUNOFF DEC is declared.

Origin: copy of the original `examples/#623 Roff/hello.roff` file.

Artefatto principale: `hello.rno`.

Control provided, from the folder of the variant:

```text
groff -Tascii hello.rno
```

Expected result: Text output contains Hello, World!..

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.gnu.org/software/groff/manual/groff.html](https://www.gnu.org/software/groff/manual/groff.html)
