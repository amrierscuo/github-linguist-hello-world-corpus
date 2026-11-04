# 0041 Assembly: variant `.a51`

Role: Assembly 8051 Keil A51; send greeting via UART (clock 11.0592 MHz, timer 1 ).

Type: **adapted**. Starting model: examples/#041 Assembly/hello.s; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
Keil A51: assemblare hello.a51; collegare e simulare un 8051 a 11.0592 MHz; acquisire l’UART.
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

- [https://sourceware.org/binutils/docs/as/i386_002dSyntax.html](https://sourceware.org/binutils/docs/as/i386_002dSyntax.html)
- [https://sourceware.org/binutils/docs/as/i386_002dOptions.html](https://sourceware.org/binutils/docs/as/i386_002dOptions.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://www.keil.com/support/man/docs/a51/](https://www.keil.com/support/man/docs/a51/)
