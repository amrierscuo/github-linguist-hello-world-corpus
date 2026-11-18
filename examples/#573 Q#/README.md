# #573 Q#

## Verified on November 18, 2026

Microsoft QDK’s Rust-backed Python interpreter loaded the original Q# source and executed Main. Message emitted the greeting.

Run `Load Main.qs with qsharp.eval and invoke Corpus.Main() on the local QDK interpreter`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Perform a classic Q# entry point that invokes Message.

## Toolchain

Q# compiler/runtime compatibile

## Procedure

Fill in Main.qs with Q# toolchain that supports @EntryPoint and register local execution.

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.



Remaining requirements:
- Local Q# compiler/runtime not predisposed; entry-point compatibility to be recorded.

## Primary sources

- [https://learn.microsoft.com/azure/quantum/user-guide/language/statements/calls](https://learn.microsoft.com/azure/quantum/user-guide/language/statements/calls)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.qs` | [Main.qs](Main.qs) Syntax and behavior verified |

</details>
