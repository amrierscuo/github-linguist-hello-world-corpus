# 0011 AMPL: variant `.mod`

Role: Textual Alias of the same format and of the same programma/dataset of the original model.

Tipo variante: **alias**. Copia byte-identica di examples/#011 AMPL/hello.ampl

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
ampl hello.mod
```

Exit 0; empty stderr; stdout exactly Hello, World! and a LF/CRLF terminator ( CRLF observed on Windows).

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://ampl.com/wp-content/uploads/Chapter-12-Display-Commands-AMPL-Book.pdf](https://ampl.com/wp-content/uploads/Chapter-12-Display-Commands-AMPL-Book.pdf)
- [https://dev.ampl.com/ampl/python/index.html](https://dev.ampl.com/ampl/python/index.html)
- [https://pypi.ampl.com/ampl-module-base/](https://pypi.ampl.com/ampl-module-base/)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
