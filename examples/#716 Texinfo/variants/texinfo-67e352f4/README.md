# 0716: Texinfo: `.texinfo`

## Latest recorded verification

**Syntax and behavior verified** for `.texinfo`. GNU Texinfo parsed and rendered the exact suffix variant as plain text containing Hello, World!, without a viewer or graphical application. [Recorded evidence](../../verification/native_20261105_batch_2e746578696e666f.json).

Textual variation of the same format, with canon suffix .texinfo.

Origin: copy of the original `examples/#716 Texinfo/hello.texi` file.

Artefatto principale: `hello.texinfo`.

Control provided, from the folder of the variant:

```text
makeinfo --plaintext --output=work/hello.txt hello.texinfo
```

Expected result: Document rendering contains Hello, World!..

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.gnu.org/software/texinfo/manual/texinfo/html_node/Short-Sample.html](https://www.gnu.org/software/texinfo/manual/texinfo/html_node/Short-Sample.html)
