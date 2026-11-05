# 0623: Roff: `.4`

## Latest recorded verification

**Syntax and behavior verified** for `.4`. Native groff rendered the exact variant using its plain, man, mdoc, me or ms input as recorded; the rendered text contains Hello, World!. Macro includes were loaded natively when present. No GUI renderer was used. [Recorded evidence](../../verification/native_20261105_batch_2e34.json).

Original man page of the 4 section; .in is a static template without replacements.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.4`.

Control provided, from the folder of the variant:

```text
groff -Tascii -man hello.4
```

Expected result: formatted text containing Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.gnu.org/software/groff/manual/groff.html](https://www.gnu.org/software/groff/manual/groff.html)
