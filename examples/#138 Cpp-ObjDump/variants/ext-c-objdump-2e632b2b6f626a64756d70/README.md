# 0138 Cpp-ObjDump: variant `.c++objdump`

Role: Disassembly objdump authentic textual of the C++ program already present: only alias of the format, not code C+++ compiled.

Tipo variante: **alias**. Copia byte-identica di examples/#138 Cpp-ObjDump/hello.cppobjdump

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
Rigenerare disassembly con objdump -d -C sul binario C++ originale in output esterno e confrontare con hello.c++objdump.
```

Expected result: Dump ELF x86_64 with <main>: and .rodata section; strings identifies Hello, World!; the executable ends 0 with greeting.

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://sourceware.org/binutils/docs/binutils/objdump.html](https://sourceware.org/binutils/docs/binutils/objdump.html)
- [https://sourceware.org/binutils/docs/binutils/strings.html](https://sourceware.org/binutils/docs/binutils/strings.html)
- [https://gcc.gnu.org/onlinedocs/gcc/Invoking-G_002b_002b.html](https://gcc.gnu.org/onlinedocs/gcc/Invoking-G_002b_002b.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
