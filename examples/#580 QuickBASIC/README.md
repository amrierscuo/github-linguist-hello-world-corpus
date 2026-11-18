# #580 QuickBASIC

## Verified on November 18, 2026

FreeBASIC compiled the original in QuickBASIC compatibility mode. The resulting native executable printed the exact greeting.

Run `fbc -lang qb hello.bas -x hello; ./hello`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

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

</details>
