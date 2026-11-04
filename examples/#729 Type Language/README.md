# #729 Type Language

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
| `.tl` | [hello.tl](hello.tl) created; verification pending |
