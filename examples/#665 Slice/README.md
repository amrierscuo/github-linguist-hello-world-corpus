# #665 Slice

## Latest recorded verification

**Syntax and behavior verified** on November 5, 2026.

The genuine ZeroC Slice compiler accepted the exact original definition, generated its C++ constant, and a native C++ program compiled against the genuine Ice SDK read Greeting::message and printed the exact greeting. The definition contains no server or proxy; no network or daemon was started.

[Native commands, versions, outputs and SHA-256](verification/native_20261105_batch_main.json).

## Extension results

- `.ice`: syntax and behavior verified.

<details>
<summary>Original instructions and earlier status</summary>

Fill out a Slice Ice definition with constant string message.

Canonical type `programming`, language_id `894641667`.

Suggested toolchain: ZeroC Ice slice2cpp and SDK Ice.

From the example directory:

```sh
slice2cpp --output-dir build hello.ice
```

Expected result: accepted and constant definition Greeting::message equal to greeting.

The file defines a constant, no server, proxy or network communications.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [Ice Slice](https://docs.zeroc.com/ice/latest/the-slice-language)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ice` | [hello.ice](hello.ice) syntax and behavior verified |

</details>
