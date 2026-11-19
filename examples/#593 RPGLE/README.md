# #593 RPGLE

## Verified on November 19, 2026

The compatible RPGLE interpreter loaded the complete source. Its DSPLY sink emitted the exact greeting.

Run `java -cp <JaRIKo dependencies> RunRpg.java <source directory>`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave800_main.json).

[Prior attempt](verification/native_20261119_wave800_prior_attempt.json).

<details>
<summary>Earlier instructions and evidence</summary>

Fill in RPGLE free-format and view your greeting with DSPLY.

Canonical type `programming`, language_id `609977990`.

Suggested toolchain: IBM i ILE RPG compiler.

From the example directory:

```sh
CRTBNDRPG PGM(TEST/HELLO) SRCSTMF(hello.rpgle)
CALL PGM(TEST/HELLO)
```

Expected result: DSPLY Hello, World! message.

Bookcase and path names must be adapted to a IBM test.

Stato iniziale: creato; sintassi e semantica in attesa. IBM i e ILE RPG compiler non disponibili.

Sources:

- [IBM RPG free form](https://www.ibm.com/docs/en/i/7.5.0?topic=specifications-fully-free-form-statements)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.rpgle` | [hello.rpgle](hello.rpgle) Syntax and behavior verified |
| `.sqlrpgle` | [hello.sqlrpgle](variants/sqlrpgle-34018e4d/hello.sqlrpgle) created; verification pending |

</details>
