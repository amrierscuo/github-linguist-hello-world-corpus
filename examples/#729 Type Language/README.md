# #729 Type Language

## Verified on November 18, 2026

Telethon compiled the unchanged Telegram TL schema into its real serializer class, then wrote and read back the exact greeting with the correct constructor identifier.

Run `python tl.py with Telethon generator and runtime`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Fill out a manufacturer in the Type Language TL of Telegram.

## Toolchain

TL compiler e runtime generato

## Procedure

Fill hello.tl with a compatible TL tool; build Greeting(text= "Hello, World!") and check roundtrip.

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.

The scheme does not invent a ID constructor: the compiler must calculate it from the canonical constructor.

Remaining requirements:
- Compiler TL/runtime per schema originale non predisposti.

## Primary sources

- [https://core.telegram.org/mtproto/TL](https://core.telegram.org/mtproto/TL)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.tl` | [hello.tl](hello.tl) Syntax and behavior verified |

</details>
