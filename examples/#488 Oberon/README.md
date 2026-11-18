# #488 Oberon

## Verified on November 18, 2026

The native Oberon-2 translator compiled the original module and linked it with the genuine standard library. The executable printed the exact greeting.

Run `voc -m -O2 Hello.ob2; ./Hello`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Perform a Oberon- 2 module that uses Out.

## Toolchain

Compilatore Oberon-2 e modulo standard Out

## Procedure

Fill in Hello.ob2 and invoke the Hello form with the Oberon- 2 runtime chosen; register the actual command.

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.

The file uses the MODULE/IMPORT/BEGIN subset common in Oberon- 2; Out is a real dependence of the chosen runtime.

Remaining requirements:
- Oberon- 2 compiler and Out library not available; comando/versione must be recorded in the future test.

## Primary sources

- [https://www.inf.ethz.ch/personal/wirth/Oberon/Oberon07.Report.pdf](https://www.inf.ethz.ch/personal/wirth/Oberon/Oberon07.Report.pdf)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ob2` | [Hello.ob2](Hello.ob2) Syntax and behavior verified |

</details>
