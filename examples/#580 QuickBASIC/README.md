# #580 QuickBASIC

Fill in and run QuickBASIC console.

## Toolchain

Microsoft QuickBASIC 4.5; DOS emulator

## Procedure

In the DOS runtime: BC HELLO.BAS; LINK HELLO.OBJ; HELLO.EXE (record opzioni/versioni actual).

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.

Original source in the PRINT/END subset; a test with other BASIC is not counted as QuickBASIC verification.

Remaining requirements:
- Compiler Microsoft QuickBASIC and runtime DOS not available.

## Primary sources

- [https://archive.org/details/ms-quickbasic-4.5](https://archive.org/details/ms-quickbasic-4.5)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.bas` | [hello.bas](hello.bas), [main.bas](variants/bi-5b4ad4e3/main.bas) created; verification pending |
| `.bi` | [hello.bi](variants/bi-5b4ad4e3/hello.bi) created; verification pending |
