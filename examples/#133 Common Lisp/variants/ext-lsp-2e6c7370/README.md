# 0133 Common Lisp: variant `.lsp`

## Latest recorded verification

**Syntax and behavior verified** for `.lsp`. SBCL natively read and executed the exact Lisp variant; when declared, ASDF loaded the original system definition and companion source. The actual script/load output includes Hello, World!. No editor or historical plugin host is implied. [Recorded evidence](../../verification/native_20261105_batch_2e6c7370.json).

Role: Common Lisp/S-expression Shapes; this suffix remains in Common Lisp, not in the omonymous dialects of other folders.

Tipo variante: **alias**. Copia byte-identica di examples/#133 Common Lisp/hello.lisp

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
sbcl --script hello.lsp
```

Exit 0; stdout Hello, World! followed by newline.

## Earlier status and evidence
Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://www.sbcl.org/manual/#Shebang-Scripts](https://www.sbcl.org/manual/#Shebang-Scripts)
- [https://www.lispworks.com/documentation/HyperSpec/Body/f_concat.htm](https://www.lispworks.com/documentation/HyperSpec/Body/f_concat.htm)
- [https://www.lispworks.com/documentation/HyperSpec/Body/22_c.htm](https://www.lispworks.com/documentation/HyperSpec/Body/22_c.htm)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
