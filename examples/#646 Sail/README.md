# #646 Sail

## Verified on November 18, 2026

The native Sail interpreter evaluated the unchanged declared string binding to the exact greeting.

Run `sail -i hello.sail (interpreter input greeting
:run)`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Check the type of the constant greeting Sail and read its value.

## Toolchain

Sail compiler/interpreter

## Procedure

sail -i hello.sail; in REPL evaluate and record actual valore/comando greeting.

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.



Remaining requirements:
- Sail compiler/prelude non predisposti; type check e REPL pending.

## Primary sources

- [https://github.com/rems-project/sail](https://github.com/rems-project/sail)
- [https://alasdair.github.io/manual.html](https://alasdair.github.io/manual.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.sail` | [hello.sail](hello.sail) Syntax and behavior verified |

</details>
