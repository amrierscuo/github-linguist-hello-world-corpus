# 0215 Forth: variant `.4th`

## Latest recorded verification

**Syntax and behavior verified** for `.4th`. Gforth loaded its original VM image, compiled and executed the exact suffix variant, and printed exactly Hello, World! plus LF without stderr. [Recorded evidence](../../verification/native_20261105_batch_2e347468.json).

Role: Textual Source Forth; .f / .for / .fs in this folder are not Fortran or F# sources.

Tipo variante: **alias**. Copia byte-identica di examples/#215 Forth/hello.fth

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
gforth hello.4th
```

Exit 0; exact greeting followed by newline.

## Earlier status and evidence
Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://www.complang.tuwien.ac.at/forth/gforth/Docs-html/](https://www.complang.tuwien.ac.at/forth/gforth/Docs-html/)
- [https://forth-standard.org/standard/core/Dotp](https://forth-standard.org/standard/core/Dotp)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
