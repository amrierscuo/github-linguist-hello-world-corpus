# 0001 1C Enterprise: variant `.bsl`

Role: BSL 1C/OneScript source module: same instruction Сообщить of the .os model; reader/runtime is explicitly invoked on the BSL file.

Tipo variante: **alias**. Copia byte-identica di examples/#001 1C Enterprise/hello.os

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
oscript hello.bsl
```

Expected result: Syntax check: exit 0, No errors; run: exit 0, exactly Hello, World! followed by newline

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://www.oscript.io/](https://www.oscript.io/)
- [https://www.oscript.io/learn/tutorial-info](https://www.oscript.io/learn/tutorial-info)
- [https://github.com/EvilBeaver/OneScript/releases/tag/v2.2.0](https://github.com/EvilBeaver/OneScript/releases/tag/v2.2.0)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
