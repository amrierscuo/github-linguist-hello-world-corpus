# 0150 Cython: variant `.pxi`

Role: Includes Cython pxi, including in the companion unit.

Type: **adapted**. Starting model: examples/#150 Cython/hello.pyx; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
Cython/setuptools: compilare consumer.pyx; python -c "import consumer"
```

Expected result: Hello, World!

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://docs.cython.org/en/latest/src/userguide/source_files_and_compilation.html](https://docs.cython.org/en/latest/src/userguide/source_files_and_compilation.html)
- [https://github.com/cython/cython](https://github.com/cython/cython)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://cython.readthedocs.io/en/latest/src/userguide/language_basics.html](https://cython.readthedocs.io/en/latest/src/userguide/language_basics.html)
