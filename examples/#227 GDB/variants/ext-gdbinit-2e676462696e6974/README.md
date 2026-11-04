# 0227 GDB: variant `.gdbinit`

Role: GDB commands that can be loaded as an explicit initialization file; no global init change.

Tipo variante: **alias**. Copia byte-identica di examples/#227 GDB/hello.gdb

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
gdb -q -nx -batch -x hello.gdbinit
```

Expected result: stdout exactly Hello, World! followed by newline; exit 0.

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://www.gnu.org/software/gdb/documentation/](https://www.gnu.org/software/gdb/documentation/)
- [https://sourceware.org/gdb/current/onlinedocs/gdb.html/Output.html](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Output.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
