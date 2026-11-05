# 0271 Graphviz (DOT): variant `.gv`

## Latest recorded verification

**Syntax and behavior verified** for `.gv`. Graphviz natively parsed and laid out the exact .gv file; the resulting SVG contains a text node exactly Hello, World!. Rendering stayed in files without a viewer. [Recorded evidence](../../verification/native_20261105_batch_2e6776.json).

Role: Textual Alias of the same format and of the same programma/dataset of the original model.

Tipo variante: **alias**. Copia byte-identica di examples/#271 Graphviz (DOT)/hello.dot

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
dot -Tsvg hello.gv -o <output>/hello.svg; controllare il testo del nodo nel SVG.
```

Expected result: SVG valid with Hello, World! text; PASS.

## Earlier status and evidence
Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://www.graphviz.org/doc/info/lang.html](https://www.graphviz.org/doc/info/lang.html)
- [https://graphviz.org/docs/outputs/svg/](https://graphviz.org/docs/outputs/svg/)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
