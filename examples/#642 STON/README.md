# #642 STON

## Verified on November 18, 2026

Pharo’s native STON library decoded the exact document and returned the exact greeting from its dictionary.

Run `pharo --headless Pharo.image st check.st --quit`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Read a STON map in Smalltalk.

## Toolchain

STON originale su Pharo/Squeak

## Procedure

STON fromString: (FileSystem workingDirectory / 'hello.ston') contents; leggere la chiave greeting.

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.



Remaining requirements:
- VM Smalltalk e libreria STON non predisposte.

## Primary sources

- [https://github.com/svenvc/ston/blob/master/ston-spec.md](https://github.com/svenvc/ston/blob/master/ston-spec.md)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ston` | [hello.ston](hello.ston) Syntax and behavior verified |

</details>
