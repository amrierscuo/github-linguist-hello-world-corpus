# 0085 C++: variant `.tcc`

## Latest recorded verification

**Syntax and behavior verified** for `.tcc`. Variant only. Main language status and other suffixes unchanged. [Recorded evidence](../../verification/native_20261104_followup_2e746363.json).

Ruolo: Implementazione di template C++ inclusa.

Type: **adapted**. Starting model: examples/#085 C++/hello.cpp; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
g++ -std=c++17 consumer.cpp -o <output>/hello; <output>/hello
```

Expected result: Hello, World!

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
- [https://isocpp.org/faq/templates](https://isocpp.org/faq/templates)
