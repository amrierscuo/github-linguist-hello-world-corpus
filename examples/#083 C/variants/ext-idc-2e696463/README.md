# 0083 C: variant `.idc`

Role: Script IDC for IDA: API Message and main entry point of runtime IDC.

Type: **adapted**. Starting model: examples/#083 C/hello.c; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
IDA in ambiente di prova: eseguire hello.idc con il motore IDC e leggere il messaggio nella console.
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

- [https://gcc.gnu.org/onlinedocs/gcc/Standards.html](https://gcc.gnu.org/onlinedocs/gcc/Standards.html)
- [https://www.gnu.org/software/libc/manual/html_node/Simple-Output.html](https://www.gnu.org/software/libc/manual/html_node/Simple-Output.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://docs.hex-rays.com/developer-guide/idc](https://docs.hex-rays.com/developer-guide/idc)
