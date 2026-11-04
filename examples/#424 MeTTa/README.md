# #424 MeTTa

## Latest recorded verification

**Syntax and behavior verified** on November 4, 2026.

The official native Hyperon Python binding evaluated the exact MeTTa program, with the exact greeting and LF and no stderr.

[Native commands, versions, outputs and SHA-256](verification/native_20261104_followup_main.json).

## Extension results

- `.metta`: syntax and behavior verified.

<details>
<summary>Original instructions and earlier status</summary>

Execute a MeTTa expression that calls println! with greeting.

Canonical type `programming`, language_id `1037612668`.

Suggested toolchain: Python 3.13 and Hyperon MeTTa original.

From the example directory:

```sh
python verify.py
```

Expected result: stdout Hello, World! and LF, no MeTTa error.

The binding performs the original program with the standard engine library.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [Hyperon — implementazione MeTTa](https://github.com/trueagi-io/hyperon-experimental)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.metta` | [hello.metta](hello.metta) syntax and behavior verified |

</details>
