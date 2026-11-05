# #105 Cairo

## Latest recorded verification

**Syntax and behavior verified** on November 5, 2026.

Pinned Scarb compiled the unchanged Cairo executable project and cairo_execute ran it, producing the exact greeting line. No Starknet contract, wallet or network transaction was involved.

[Native commands, versions, outputs and SHA-256](verification/native_20261105_target546_main.json).

Current native command or procedure: `scarb build; scarb execute (use the pinned project manifest and Scarb 2.11.4 recorded in the receipt)`.

## Extension results

- `.cairo`: syntax and behavior verified.

<details>
<summary>Original instructions and earlier status</summary>

Fill out and execute a modern Cairo program that prints Hello, World!.

Canonical type: `programming`; `language_id`: `620599567`.

Suggested toolchain: Scarb 2.11.4 with cairo_execute 2.11.4 (project fixed to the version of the guide).

From the example folder, depending on the PATH:

```sh
scarb build
scarb execute
```

Expected result: between Scarb messages, a `Hello, World!` line and 0. output

Cairo modern and Cairo Zero are separate voices of the reference.This project uses the executable and Scarb attribute; it is not a Starknet contract.

Initial state: artifact created, syntax and behavioral verification pending. Specific toolchain not yet performed on this example; syntax and behavior remain to be checked.

Primary sources or original references of the project:

- [Cairo Book — Hello, World](https://www.starknet.io/cairo-book/ch01-02-hello-world.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cairo` | [lib.cairo](src/lib.cairo) syntax and behavior verified |

</details>
