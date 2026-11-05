# #722 Toit

## Latest recorded verification

**Syntax and behavior verified** on November 5, 2026.

The official native Toit2.0 compiler/runtime compiled and ran the exact original main/print source on Linux and emitted exactly the greeting and LF. No embedded device, cloud service or GUI was used.

[Native commands, versions, outputs and SHA-256](verification/native_20261105_target546_main.json).

Current native command or procedure: `toit.run hello.toit`.

## Extension results

- `.toit`: syntax and behavior verified.

<details>
<summary>Original instructions and earlier status</summary>

Run the original Toit program.

## Toolchain

Toit compiler/runtime

## Procedure

toit run hello.toit

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.



Remaining requirements:
- Runtime Toit not predisposed; sintassi/versione CLI to check.

## Primary sources

- [https://docs.toit.io/language/](https://docs.toit.io/language/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.toit` | [hello.toit](hello.toit) syntax and behavior verified |

</details>
