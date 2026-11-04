# 0830: reStructuredText: `.rst.txt`

## Latest recorded verification

**Syntax and behavior verified** for `.rst.txt`. Docutils: original AST and HTML5 renderer preserve exact paragraph and inline emphasis. [Recorded evidence](../../verification/native_20261104_followup_2e7273742e747874.json).

Textual variation of the same format, with canon suffix .rst.txt.

Origin: copy of the original `examples/#830 reStructuredText/hello.rst` file.

Artefatto principale: `hello.rst.txt`.

Control provided, from the folder of the variant:

```text
docutils: render hello.rst.txt and assert the greeting paragraph
```

Expected result: Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html)
