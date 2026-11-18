# #804 Zeek

## Verified on November 18, 2026

A pinned published binary closure provided the native command-line runtime, which evaluated the unchanged original source and emitted the exact greeting.

Run `zeek -b hello.zeek`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Run zeek_init without network capture.

## Toolchain

Zeek runtime

## Procedure

zeek hello.zeek

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.

Only start of the local script, no capture interface or network.

Remaining requirements:
- Zeek parser/runtime unavailable.

## Primary sources

- [https://docs.zeek.org/en/current/scripting/basics.html](https://docs.zeek.org/en/current/scripting/basics.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.zeek` | [hello.zeek](hello.zeek) Syntax and behavior verified |
| `.bro` | [hello.bro](variants/bro-c936c4b3/hello.bro) created; verification pending |

</details>
