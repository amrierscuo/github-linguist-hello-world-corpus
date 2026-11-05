# 0624: Roff Manpage: `.5`

## Latest recorded verification

**Syntax and behavior verified** for `.5`. Native groff rendered the exact variant using its plain, man, mdoc, me or ms input as recorded; the rendered text contains Hello, World!. Macro includes were loaded natively when present. No GUI renderer was used. [Recorded evidence](../../verification/native_20261105_batch_2e35.json).

Original man page of the 5 section; .in is a static template without replacements.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.5`.

Control provided, from the folder of the variant:

```text
groff -Tascii -man hello.5
```

Expected result: formatted text containing Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.gnu.org/software/groff/manual/groff.html](https://www.gnu.org/software/groff/manual/groff.html)
