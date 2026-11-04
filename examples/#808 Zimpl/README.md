# #808 Zimpl

Generate and solve a LP Zimpl whose excellent encodes greeting bytes.

## Toolchain

Zimpl; LP solver

## Procedure

zimpl -o build/hello hello.zpl; glpsol --lp build/hello.lp; read and decode the optimal x[i].

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.

Original indexed variables have bounds [ ASCII, ASCII + 1 ]; the minimizing objective must choose the lower codes.

Remaining requirements:
- Zimpl compiler unavailable nei pacchetti isolati; parsing/generazione LP e soluzione pending.

## Primary sources

- [https://zimpl.zib.de/](https://zimpl.zib.de/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.zimpl` | [hello.zimpl](variants/zimpl-c607d319/hello.zimpl) created; verification pending |
| `.zmpl` | [hello.zmpl](variants/zmpl-c5eac23d/hello.zmpl) created; verification pending |
| `.zpl` | [hello.zpl](hello.zpl) created; verification pending |
