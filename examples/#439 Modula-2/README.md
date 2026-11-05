# #439 Modula-2

## Latest recorded verification

**Syntax and behavior verified** on November 5, 2026.

GNU Modula-2 compiled the exact PIM module and its native executable printed the exact greeting with LF.

[Native commands, versions, outputs and SHA-256](verification/native_20261105_batch_main.json).

## Extension results

- `.mod`: syntax and behavior verified.

<details>
<summary>Original instructions and earlier status</summary>

Fill out Modula- 2 with PIM InOut library and print your greeting.

Canonical type `programming`, language_id `234`.

Suggested toolchain: GNU Modula- 2 gm2 with PIM libraries.

From the example directory:

```sh
gm2 -fpim Hello.mod -o hello
./hello
```

Expected result: stdout Hello, World! and newline.

The InOut library is of the PIM family; the toolchain must use the corresponding dialect.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [GNU Modula-2 — manuale](https://gcc.gnu.org/onlinedocs/gm2/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mod` | [Hello.mod](Hello.mod) syntax and behavior verified |

</details>
