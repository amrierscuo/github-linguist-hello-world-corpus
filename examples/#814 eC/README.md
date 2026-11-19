# #814 eC

## Verified on November 19, 2026

The publisher compiler compiled the unchanged eC program using a disposable project fixture. The native Windows console executable emitted the exact greeting.

Run `epj2make hello.epj; mingw32-make -f hello.Makefile; run the generated Windows console application`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave800_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Fill eC Ecere and run Main.

## Toolchain

Ecere SDK eC compiler

## Procedure

Fill hello.ec in an Ecere console project; record ecc/ecp/linker and start the result.

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.



Remaining requirements:
- Ecere compiler/SDK non predisposti.

## Primary sources

- [https://www.ecere.org/](https://www.ecere.org/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ec` | [hello.ec](hello.ec) Syntax and behavior verified |
| `.eh` | [hello.eh](variants/eh-5ad89293/hello.eh) created; verification pending |

</details>
