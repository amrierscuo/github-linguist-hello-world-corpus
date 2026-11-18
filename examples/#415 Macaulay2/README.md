# #415 Macaulay2

## Verified on November 18, 2026

Macaulay2 executed the unchanged course source and printed the exact greeting. Its packaged singular data were mounted read-only in a private namespace.

Run `M2 --script hello.m2`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Stampare Hello, World! in Macaulay2.

Canonical type `programming`, language_id `34167825`.

Suggested toolchain: Macaulay2 M2 CLI.

From the example directory:

```sh
M2 --script hello.m2
```

Expected result: stdout Hello, World! and LF.

The print form does not require you to build rings or install additional packages.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [Macaulay2 — print](https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Macaulay2Doc/html/_print.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.m2` | [hello.m2](hello.m2) Syntax and behavior verified |

</details>
