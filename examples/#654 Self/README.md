# #654 Self

## Verified on November 19, 2026

The upstream Self VM initialized the standard world without graphics and evaluated the unchanged hello.self file. Its printLine message emitted the exact greeting on the VM output stream (captured as stderr), and the VM exited successfully.

Run `printf '_Quit.\n' > exit-self.self && Self -f /path/to/Self/objects/worldBuilder.self -b /path/to/Self/objects -o none -f2 hello.self -f3 exit-self.self`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave800_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Evaluate a printLine message in the standard Self world.

## Toolchain

Self VM e standard world

## Procedure

In the standard world Self evaluate hello.self via fileIn; record VM/world and output.

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.



Remaining requirements:
- VM Self e standard world non predisposti.

## Primary sources

- [https://handbook.selflanguage.org/](https://handbook.selflanguage.org/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.self` | [hello.self](hello.self) Syntax and behavior verified |

</details>
