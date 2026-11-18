# #822 mcfunction

## Verified on November 19, 2026

The compatible interpreter loaded the exact function as a datapack entry, executed data modify storage, and read the greeting back under the declared corpus:hello storage key.

Run `mcfun (REPL: load pack, run corpus:hello, storage, stats)`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave756_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

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
| `.mcfunction` | [hello.mcfunction](hello.mcfunction) Syntax and behavior verified |

</details>
