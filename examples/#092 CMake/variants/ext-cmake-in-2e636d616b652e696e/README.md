# 0092 CMake: variant `.cmake.in`

Ruolo: Template CMake configurato con configure_file @ONLY.

Type: **adapted**. Starting model: examples/#092 CMake/hello.cmake; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
cmake -DOUT=<output> -P configure.cmake; cmake -P <output>/hello.cmake
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

- [https://cmake.org/cmake/help/latest/manual/cmake.1.html](https://cmake.org/cmake/help/latest/manual/cmake.1.html)
- [https://cmake.org/cmake/help/latest/command/message.html](https://cmake.org/cmake/help/latest/command/message.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://cmake.org/cmake/help/latest/command/configure_file.html](https://cmake.org/cmake/help/latest/command/configure_file.html)
