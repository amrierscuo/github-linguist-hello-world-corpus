# 0256 Gnuplot: variant `.p`

Role: Textual Alias of the same format and of the same programma/dataset of the original model.

Tipo variante: **alias**. Copia byte-identica di examples/#256 Gnuplot/hello.gnuplot

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
gnuplot hello.p
```

Exit 0; graph ASCII contains the title Hello, World! and the y=x line.

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://www.gnuplot.info/documentation.html](https://www.gnuplot.info/documentation.html)
- [https://gnuplot.sourceforge.net/docs/loc18701.html](https://gnuplot.sourceforge.net/docs/loc18701.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
