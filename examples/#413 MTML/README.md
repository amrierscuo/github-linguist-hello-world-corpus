# #413 MTML

## Verified on November 18, 2026

Movable Type compiled and rendered the unchanged original template. The template’s variable assignment and lookup produced the greeting.

Run `perl render.pl with Movable Type Perl libraries`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Assign a MTML variable and make Hello, World!.

Canonical type `markup`, language_id `218`.

Toolchain provided: Movable Type template engine.

From the example directory:

```sh
Renderizzare hello.mtml con il motore template Movable Type locale.
```

Expected result: Hello, World! output and newline.

The Var assignment with value does not produce output. Reading without value produces the name; it is not enough to interpret the document as HTML.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [Movable Type — Var](https://www.movabletype.org/documentation/appendices/tags/var.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mtml` | [hello.mtml](hello.mtml) Syntax and behavior verified |

</details>
