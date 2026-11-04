# 0063 BibTeX: variant `.bibtex`

Role: a textual BibTeX database, not an AUX file or BST style.

Tipo variante: **alias**. Copia byte-identica di examples/#063 BibTeX/hello.bib

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
Copiare il driver AUX in output esterno, indirizzare \bibdata a hello.bibtex; bibtex sul driver.
```

Expected result: driver.bbl contains the title { Hello, World! }; exit 0.

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://ctan.org/pkg/bibtex](https://ctan.org/pkg/bibtex)
- [https://mirrors.ctan.org/biblio/bibtex/base/btxdoc.pdf](https://mirrors.ctan.org/biblio/bibtex/base/btxdoc.pdf)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
