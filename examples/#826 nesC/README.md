# #826 nesC

## Verified on November 19, 2026

The native nesC compiler resolved the original component wiring. A headless test platform signalled the TinyOS Boot interface and the original handler wrote and flushed the greeting through the test platform serial adapter.

Run `nescc -I. -fnesc-target=env HelloAppC.nc -o hello && ./hello`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave800_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Fill in a nesC TinyOS configuration and record your greeting from Boot.

## Toolchain

nesC; TinyOS; piattaforma/simulatore

## Procedure

In the context of TinyOS with MAKERULES/TOSROOT configured: make <target-di-prova>; start and read the printf channel.

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.



Remaining requirements:
- nesC/TinyOS compiler, components and test targets not available.

## Primary sources

- [https://github.com/tinyos/nesc](https://github.com/tinyos/nesc)
- [https://github.com/tinyos/tinyos-main](https://github.com/tinyos/tinyos-main)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.nc` | [HelloAppC.nc](HelloAppC.nc), [HelloC.nc](HelloC.nc) Syntax and behavior verified |

</details>
