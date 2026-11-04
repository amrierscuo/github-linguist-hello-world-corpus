# #405 M4

Expand a macro GNU M4 to compose Hello, World!.

Canonical type `programming`, language_id `215`.

Suggested toolchain: GNU M4.

From the example directory:

```sh
m4 hello.m4
```

Expected result: stdout Hello, World! and LF.

The macro target is expanded by the real M4 processor.

Recorded status: syntax verified; behavior verified. Toolchain: GNU M4 extracted Ubuntu package. [Log](verification/result.json).

Sources:

- [GNU M4 — manuale](https://www.gnu.org/software/m4/manual/m4.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.m4` | [hello.m4](hello.m4) verified |
| `.mc` | [hello.mc](variants/mc-77075759/hello.mc) created; verification pending |
