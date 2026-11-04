# 0085 C++: variant `.cp`

## Latest recorded verification

**Syntax and behavior verified** for `.cp`. Variant only. Main language status and other suffixes unchanged. [Recorded evidence](../../verification/native_20261104_followup_2e6370.json).

Role: Textual Alias of the same format and of the same programma/dataset of the original model.

Tipo variante: **alias**. Copia byte-identica di examples/#085 C++/hello.cpp

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
g++ -x c++ hello.cp -o <output>/hello; <output>/hello
```

Expected result: Exit 0; exit program 0, stdout Hello, World! plus newline.

## Earlier status and evidence
Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://gcc.gnu.org/onlinedocs/gcc/Standards.html](https://gcc.gnu.org/onlinedocs/gcc/Standards.html)
- [https://www.open-std.org/jtc1/sc22/wg21/](https://www.open-std.org/jtc1/sc22/wg21/)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
