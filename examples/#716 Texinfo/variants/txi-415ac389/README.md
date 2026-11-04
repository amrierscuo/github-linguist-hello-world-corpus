# 0716: Texinfo: `.txi`

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
