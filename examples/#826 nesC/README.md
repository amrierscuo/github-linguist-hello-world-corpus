# #826 nesC

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
| `.nc` | [HelloAppC.nc](HelloAppC.nc), [HelloC.nc](HelloC.nc) created; verification pending |
