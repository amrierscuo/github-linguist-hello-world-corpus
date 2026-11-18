# #664 Slash

## Verified on November 18, 2026

The published Slash VM executed the unchanged original template and rendered the exact greeting.

Run `slash hello.sl`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Evaluate a Slash template and make greetings.

Canonical type `programming`, language_id `349`.

Suggested toolchain: Slash CLI SAPI original.

From the example directory:

```sh
slash-cli hello.sl
```

Expected result: stdout Hello, World! and newline.

The template uses the output expression of Slash; Ruby ERB does not verify its engine.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [Slash](https://github.com/slash-lang/slash)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.sl` | [hello.sl](hello.sl) Syntax and behavior verified |

</details>
