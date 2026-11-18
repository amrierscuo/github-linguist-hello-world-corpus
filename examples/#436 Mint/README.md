# #436 Mint

## Verified on November 18, 2026

Mint compiled the original component, and evaluating the emitted browser code in a headless DOM rendered the expected paragraph.

Run `mint build; node render.cjs with jsdom`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

[Prior attempt](verification/native_20261118_wave736_prior_attempt.json).

<details>
<summary>Earlier instructions and evidence</summary>

Fill out a Main Mint component and show greeting in a paragraph.

Canonical type `programming`, language_id `968740319`.

Suggested toolchain: Mint compiler compatible with the syntax typed Html.

From the example directory:

```sh
mint build
```

Expected result: successful compilation; application shows Hello, World!.

The syntax Html is documented in the guide; the compatibility with the available compiler version must be verified.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [Mint — Main component](https://api.mint-lang.com/guide/getting-started/the-main-component)
- [Mint — implementazione](https://github.com/mint-lang/mint)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mint` | [Main.mint](source/Main.mint) Syntax and behavior verified |

</details>
