# 0135 Component Pascal: variant `.cps`

Role: Textual Alias of the same format and of the same programma/dataset of the original model.

Tipo variante: **alias**. Copia byte-identica di examples/#135 Component Pascal/Hello.cp

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
BlackBox Component Builder: importare il sorgente hello.cps e invocare il comando esportato del modulo originale.
```

Expected result: Filled form; Hello.Say command available; log with Hello, World! and newline.

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://blackboxframework.org/](https://blackboxframework.org/)
- [https://github.com/BlackBoxCenter/blackbox](https://github.com/BlackBoxCenter/blackbox)
- [https://www.oberon.ch/pdf/CP-Lang.pdf](https://www.oberon.ch/pdf/CP-Lang.pdf)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
