# #667 Slint

## Verified on November 18, 2026

The native Slint runtime loaded the untouched component. Its message property and its rendered text in a private framebuffer both matched the greeting.

Run `xvfb-run -a node check.mjs; tesseract frame.png stdout --psm 11`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Fill out a Slint component with Message and Text properties connected to greeting.

Canonical type `markup`, language_id `119900149`.

Suggested toolchain: Slint compiler/interpreter.

From the example directory:

```sh
slint-viewer hello.slint
```

Expected result: accepted component and greeting display.

For visual behavior, the UI backend is used. The corpus does not open windows during a syntax control.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [Slint language](https://docs.slint.dev/latest/docs/slint/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.slint` | [hello.slint](hello.slint) Syntax and behavior verified |

</details>
