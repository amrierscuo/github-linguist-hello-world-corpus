# 0243 Gerber Image: variant `.gts`

Role: Alias conventional Gerber RS - 274X: same vector image, not Excellon/NC. The suffix is not used to declare functions or completeness of a PCB card; the Linguist .ncl sample contains the same grammar RS - 274X.

Tipo variante: **alias**. Copia byte-identica di examples/#243 Gerber Image/hello.gbr

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
PyGerber originale: caricare hello.gts come Gerber RS-274X, renderizzare e verificare visivamente Hello, World!.
```

Expected result: Parser without errors; PNG law Hello, World! with comma and exclamation point.

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://www.ucamco.com/en/gerber/downloads](https://www.ucamco.com/en/gerber/downloads)
- [https://github.com/Argmaster/pygerber](https://github.com/Argmaster/pygerber)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
