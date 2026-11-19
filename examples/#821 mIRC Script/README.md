# #821 mIRC Script

## Verified on November 19, 2026

The upstream headless engine loaded the unchanged .mrc as a script, ran its hello alias, and returned the exact echo text to the batch harness.

Run `cargo build --offline --release --bin run_greeting; run_greeting hello.mrc`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave800_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Upload an alias mIRC that writes greeting in the local window.

## Toolchain

mIRC Script runtime

## Procedure

In mIRC caricare hello.mrc con /load -rs; invocare /hello.

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.

echo -a produces local output; the sample does not send messages or start connections.

Remaining requirements:
- mIRC runtime unavailable.

## Primary sources

- [https://www.mirc.com/help/html/aliases.html](https://www.mirc.com/help/html/aliases.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mrc` | [hello.mrc](hello.mrc) Syntax and behavior verified |

</details>
