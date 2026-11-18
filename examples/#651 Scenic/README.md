# #651 Scenic

## Verified on November 18, 2026

The authentic Scenic compiler evaluated the original parameter and generated a scene carrying its exact greeting.

Run `Use scenic.syntax.translator.scenarioFromFile("hello.scenic"), generate a scene and assert scene.params["greeting"]`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Fill out a Scenic scenario that exposes a parameter of greeting.

## Toolchain

Scenic scenario compiler

## Procedure

scenic hello.scenic; check the greeting parameter in the compiled scenario.

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.

The goal is the string parameter of the scenario; no physical simulation is invented.

Remaining requirements:
- Scenic compiler/simulator non predisposti.

## Primary sources

- [https://docs.scenic-lang.org/en/latest/syntax_guide.html](https://docs.scenic-lang.org/en/latest/syntax_guide.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.scenic` | [hello.scenic](hello.scenic) Syntax and behavior verified |

</details>
