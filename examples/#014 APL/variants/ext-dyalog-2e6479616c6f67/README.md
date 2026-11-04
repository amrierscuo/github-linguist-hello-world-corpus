# 0014 APL: variant `.dyalog`

Role: Textual Source APL/Dyalog, not a DWS binary workspace.

Tipo variante: **alias**. Copia byte-identica di examples/#014 APL/hello.apl

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
Dyalog: caricare hello.dyalog come sorgente testuale e valutare il corpo nel workspace di prova.
```

Exit 0; vacuum stderr; stdout exactly Hello, World! and a LF/CRLF terminator ( CRLF observed on Windows) in dzaima/APL. dialect

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://github.com/dzaima/APL](https://github.com/dzaima/APL)
- [https://github.com/dzaima/APL/blob/5eb0a4205e27afa6122096a25008474eec562dc0/build](https://github.com/dzaima/APL/blob/5eb0a4205e27afa6122096a25008474eec562dc0/build)
- [https://github.com/dzaima/APL/blob/5eb0a4205e27afa6122096a25008474eec562dc0/src/APL/Main.java](https://github.com/dzaima/APL/blob/5eb0a4205e27afa6122096a25008474eec562dc0/src/APL/Main.java)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
