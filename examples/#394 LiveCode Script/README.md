# #394 LiveCode Script

## Verified on November 19, 2026

The published headless LiveCode engine loaded the original script-only stack. Its original handler emitted the exact greeting.

Run `livecode-server driver.lc`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave800_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Upload a script-only LiveCode stack and invoke helloWorld.

## Toolchain

LiveCode Script engine; versione da registrare

## Commands and procedure

In LiveCode load the script-only hello.livecodescript stack; invoke helloWorld from Message Box on the stack

## Expected result

Handler put writes Hello, World! in the Message Box.

## Status

Syntax and behavioral verification pending.

HelloWorld script identifies a script-only stack; greeting is in the original manager.The runtime/compatibilità of the version must be recorded before the positive claim.

Remaining requirements:
- Engine LiveCode not predisposed; loading stack and handler pending.

## Primary sources

- [https://docs.livecode.com/](https://docs.livecode.com/)
- [https://github.com/livecode/livecode](https://github.com/livecode/livecode)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.livecodescript` | [hello.livecodescript](hello.livecodescript) Syntax and behavior verified |

</details>
