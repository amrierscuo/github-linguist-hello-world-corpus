# 0272 Groovy: variant `.gvy`

## Recorded verification

**Syntax and behavior verified** on November 4, 2026. Execute unchanged Groovy source and unchanged GString/Simple template drivers. Aggregate .groovy preserves the prior unchanged main proof. [Evidence](../../verification/native_20261104_272_variants_result.json).

Role: Textual Alias of the same format and of the same programma/dataset of the original model.

Tipo variante: **alias**. Copia byte-identica di examples/#272 Groovy/hello.groovy

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
groovy hello.gvy
```

Exit 0; exact greeting followed by newline.

## Earlier status
Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://groovy-lang.org/syntax.html#_string_interpolation](https://groovy-lang.org/syntax.html#_string_interpolation)
- [https://groovy-lang.org/](https://groovy-lang.org/)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
