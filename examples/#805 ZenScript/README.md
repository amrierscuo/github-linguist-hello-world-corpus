# #805 ZenScript

## Verified on November 19, 2026

The upstream ZenScript compiler emitted and loaded JVM bytecode for the original script. Executing it called the host println global with the exact greeting.

Run `javac -cp <ZenScript dependencies> -d classes @upstream-sources.txt ZenCheck.java && java -cp classes:<ZenScript dependencies> stanhebben.zenscript.ZenCheck hello.zs`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave756_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Load the ZenScript greeting script to CraftTweaker.

## Toolchain

CraftTweaker ZenScript compatibile

## Procedure

Insert hello.zs into the scripts folder of the test Minecraft/CraftTweaker profile; reload and read the log.

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.

The sample chooses ZenScript CraftTweaker1.12 with println; no recipe or external content is modified.

Remaining requirements:
- CraftTweaker/Minecraft runtime unavailable; versione ZenScript da registrare.

## Primary sources

- [https://docs.blamejared.com/1.12/en/Getting_Started/](https://docs.blamejared.com/1.12/en/Getting_Started/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.zs` | [hello.zs](hello.zs) Syntax and behavior verified |

</details>
