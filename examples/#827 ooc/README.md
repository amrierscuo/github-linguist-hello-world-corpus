# #827 ooc

## Verified on November 18, 2026

The official Rock bootstrap and shipped ooc standard library compiled the original program. Its native executable printed the greeting.

Run `hello `.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Fill ooc and call println on the string.

## Toolchain

rock ooc compiler; SDK

## Procedure

rock hello.ooc; start the compiled program.

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.



Remaining requirements:
- rock compiler/SDK not predisposed.

## Primary sources

- [https://ooc-lang.org/docs/](https://ooc-lang.org/docs/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ooc` | [hello.ooc](hello.ooc) Syntax and behavior verified |

</details>
