# 0041 Assembly: variant `.i`

Role: GNU assembly source already free of pre-processor macros; .i indicates here the pre-processed text input.

Tipo variante: **alias**. Copia byte-identica di examples/#041 Assembly/hello.s

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
as --64 hello.i -o <output>/hello.o; ld <output>/hello.o -o <output>/hello; <output>/hello
```

Exit 0; stdout exactly Hello, World! followed by newline.

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://sourceware.org/binutils/docs/as/i386_002dSyntax.html](https://sourceware.org/binutils/docs/as/i386_002dSyntax.html)
- [https://sourceware.org/binutils/docs/as/i386_002dOptions.html](https://sourceware.org/binutils/docs/as/i386_002dOptions.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
