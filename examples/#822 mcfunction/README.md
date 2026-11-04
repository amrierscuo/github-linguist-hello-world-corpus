# #822 mcfunction

Write greetings in storage of a Minecraft Java datapack.

## Toolchain

Minecraft Java command parser/runtime

## Procedure

Insert hello.mcfunction into a compatible datapack; perform /function corpus:hello and /data get storage corpus:hello greeting.

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.

The goal is a local string in the storage of the test world, without chat messages or external connections.

Remaining requirements:
- Minecraft Java runtime/datapack trial unavailable.

## Primary sources

- [https://minecraft.wiki/w/Commands/data](https://minecraft.wiki/w/Commands/data)
- [https://www.minecraft.net/en-us/article/minecraft-java-edition-1-21](https://www.minecraft.net/en-us/article/minecraft-java-edition-1-21)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mcfunction` | [hello.mcfunction](hello.mcfunction) created; verification pending |
