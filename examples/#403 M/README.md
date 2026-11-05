# #403 M

## Latest recorded verification

**Syntax and behavior verified** on November 5, 2026.

Native FIS-GT.M compiled and ran the exact M bytes after the documented HELLO.m filename staging. No database access or server was used.

[Native commands, versions, outputs and SHA-256](verification/native_20261105_batch_main.json).

## Extension results

- `.mumps`: syntax and behavior verified.

<details>
<summary>Original instructions and earlier status</summary>

Perform a M/MUMPS routine that writes greeting.

Canonical type `programming`, language_id `214`.

Suggested toolchain: YottaDB or GT.M with M enabled routine.

From the example directory:

```sh
yottadb -run HELLO
```

Expected result: stdout Hello, World! and LF.

In M the initial space distinguishes the commands from the labels. For the runtime to install the routine as HELLO.m in a dedicated routine directory; the .mumps remains the canon artifact.

Stato iniziale: creato; sintassi e semantica in attesa. Runtime YottaDB/GT.M non ancora disponibile.

Sources:

- [YottaDB — programmare in M](https://docs.yottadb.com/ProgrammersGuide/langfeat.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mumps` | [hello.mumps](hello.mumps) syntax and behavior verified |
| `.m` | [hello.m](variants/m-f7140aa0/hello.m) created; verification pending |

</details>
