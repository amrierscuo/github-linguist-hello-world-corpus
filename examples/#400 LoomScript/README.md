# #400 LoomScript

Launch an original LoomScript application and draw the greeting from run.

## Toolchain

LoomSDK storico; versione da registrare

## Commands and procedure

Insert HelloWorld.ls as the main class of the Loom project; loom build; loom run

## Expected result

run invoca base initialization e trace emette Hello, World!.

## Status

Syntax and behavioral verification pending.

It is the LoomScript language of the Loom Native SDK for applicazioni/giochi. The class extends loom.Application and keeps super.run as indicated by the vendor code. It is not a SDK blockchain of the same name.

Remaining requirements:
- Loom compiler/runtime storico non predisposto; build/avvio applicazione pending.

## Primary sources

- [https://github.com/LoomSDK/LoomSDK](https://github.com/LoomSDK/LoomSDK)
- [https://github.com/LoomSDK/LoomSDK/blob/master/sdk/src/loom/Application.ls](https://github.com/LoomSDK/LoomSDK/blob/master/sdk/src/loom/Application.ls)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ls` | [HelloWorld.ls](HelloWorld.ls) created; verification pending |
