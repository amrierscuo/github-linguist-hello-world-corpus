# #331 Janet

Stampare Hello, World! usando Janet.

Canonical type `programming`, language_id `1028705371`.

Suggested toolchain: Janet CLI original.

From the example directory:

```sh
janet hello.janet
```

Expected result: stdout Hello, World! and LF, 0. output

Program without external dependencies.

Recorded status: syntax verified; behavior verified. Toolchain: Janet 1.42.1 official Linux x64 release. [Log](verification/result.json).

Sources:

- [Janet — manuale](https://janet-lang.org/docs/)
- [Janet — sorgenti e release](https://github.com/janet-lang/janet)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.janet` | [hello.janet](hello.janet) verified |
