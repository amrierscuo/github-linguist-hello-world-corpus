# 0716: Texinfo: `.txi`

## Latest recorded verification

**Syntax and behavior verified** for `.txi`. GNU Texinfo parsed and rendered the exact suffix variant as plain text containing Hello, World!, without a viewer or graphical application. [Recorded evidence](../../verification/native_20261105_batch_2e747869.json).

Textual variation of the same format, with canon suffix .txi.

Origin: copy of the original `examples/#716 Texinfo/hello.texi` file.

Artefatto principale: `hello.txi`.

Control provided, from the folder of the variant:

```text
makeinfo --plaintext --output=work/hello.txt hello.txi
```

Expected result: Document rendering contains Hello, World!..

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.gnu.org/software/texinfo/manual/texinfo/html_node/Short-Sample.html](https://www.gnu.org/software/texinfo/manual/texinfo/html_node/Short-Sample.html)
