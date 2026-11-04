# 0791: XSLT: `.xslt`

## Latest recorded verification

**Syntax and behavior verified** for `.xslt`. libxslt via lxml: compile stylesheet and apply it to the original XML; exact greeting. [Recorded evidence](../../verification/native_20261104_followup_2e78736c74.json).

Textual variation of the same format, with canon suffix .xslt.

Origin: copy of the original `examples/#791 XSLT/hello.xsl` file.

Artefatto principale: `hello.xslt`.

Control provided, from the folder of the variant:

```text
xsltproc hello.xslt input.xml
```

Expected result: Hello, World! as a textual result of transformation..

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.w3.org/TR/1999/REC-xslt-19991116](https://www.w3.org/TR/1999/REC-xslt-19991116)
