# 0048 Awk: variant `.mawk`

## Latest recorded verification

**Syntax and behavior verified** for `.mawk`. The native Awk implementation executed the exact suffix variant and emitted exactly Hello, World! plus LF without stderr. [Recorded evidence](../../verification/native_20261105_batch_2e6d61776b.json).

Role: Source AWK in subset POSIX common: concatenation of strings and print in BEGIN.

Tipo variante: **alias**. Copia byte-identica di examples/#048 Awk/hello.awk

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
mawk -f hello.mawk
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

- [https://www.gnu.org/software/gawk/manual/gawk.html](https://www.gnu.org/software/gawk/manual/gawk.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
