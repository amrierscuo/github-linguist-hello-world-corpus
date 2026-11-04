# 0083 C: variant `.cats`

Role: Code C incorporated by FFI ATS; .cats file with C grammar, not ATS source.

Tipo variante: **alias**. Copia byte-identica di examples/#083 C/hello.c

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
gcc -x c hello.cats -o <output>/hello; <output>/hello
```

Expected result: Exit 0; exit program 0 and stdout Hello, World! plus newline.

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://gcc.gnu.org/onlinedocs/gcc/Standards.html](https://gcc.gnu.org/onlinedocs/gcc/Standards.html)
- [https://www.gnu.org/software/libc/manual/html_node/Simple-Output.html](https://www.gnu.org/software/libc/manual/html_node/Simple-Output.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
