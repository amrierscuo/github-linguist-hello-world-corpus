# #437 Mirah

## Latest recorded verification

**Syntax and behavior verified** on November 5, 2026.

The original Mirah source was compiled by Mirah and its generated JVM class printed exactly Hello, World! plus LF. No Ruby substitution or GUI was used.

[Native commands, versions, outputs and SHA-256](verification/native_20261105_target546_main.json).

Current native command or procedure: `Compile hello.mirah with Mirah 0.2.1 under JDK8, then java HelloTopLevel; see the exact compiler invocation in the receipt.`.

## Extension results

- `.mirah`: syntax and behavior verified.

<details>
<summary>Original instructions and earlier status</summary>

Fill out Mirah in bytecode JVM and print your greeting.

Canonical type `programming`, language_id `232`.

Suggested toolchain: Mirah compiler and JVM compatible.

From the example directory:

```sh
mirahc hello.mirah
java Hello
```

Expected result: stdout Hello, World! and newline.

The source uses the Ruby-like Mirah form; Ruby alone does not verify its typing or JVM generation.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [Mirah — guida e compiler](https://github.com/mirah/mirah)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.druby` | [hello.druby](variants/druby-ff72b814/hello.druby) created; verification pending |
| `.duby` | [hello.duby](variants/duby-6fa18d7f/hello.duby) created; verification pending |
| `.mirah` | [hello.mirah](hello.mirah) syntax and behavior verified |

</details>
