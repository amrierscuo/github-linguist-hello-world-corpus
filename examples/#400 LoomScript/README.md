# #400 LoomScript

## Verified on November 22, 2026

The pinned LoomScript compiler built Main.loom from the unchanged HelloWorld.ls and the recorded project fixture. The native LoomPlayer ran the resulting assembly in an isolated Xvfb display. HelloWorld.run printed the exact line `Hello, World!`. The application loop was stopped after eight seconds by the test timeout, which returned 124. The log also records unavailable audio and failed connection attempts to the optional localhost asset server.

Run `cd "$LOOM_PROJECT" && mkdir -p bin && "$LOOM_LSC" --root "$LOOM_SDK/" --project "$LOOM_PROJECT" HelloWorld.build && SDL_VIDEODRIVER=x11 SDL_AUDIODRIVER=dummy LIBGL_ALWAYS_SOFTWARE=1 xvfb-run -a -s '-screen 0 640x480x24 -nolisten tcp' timeout --kill-after=3s 8s stdbuf -oL -eL "$LOOM_PLAYER" "$LOOM_PROJECT/bin/Main.loom"`.

[Commands, toolchain, output and SHA-256](verification/native_20261122_wave800_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

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
| `.ls` | [HelloWorld.ls](HelloWorld.ls) Syntax and behavior verified |

</details>
