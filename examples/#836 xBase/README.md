# #836 xBase

Fill in and run a xBase program.

## Toolchain

Harbour xBase compiler/runtime

## Procedure

hbmk2 hello.prg -obuild/hello; build/hello

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.



Remaining requirements:
- Harbour/xBase compiler/runtime non predisposti.

## Primary sources

- [https://harbour.github.io/](https://harbour.github.io/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.prg` | [hello.prg](hello.prg), [main.prg](variants/ch-20daa7ca/main.prg) created; verification pending |
| `.ch` | [hello.ch](variants/ch-20daa7ca/hello.ch) created; verification pending |
| `.prw` | [hello.prw](variants/prw-1dc8a242/hello.prw) created; verification pending |
