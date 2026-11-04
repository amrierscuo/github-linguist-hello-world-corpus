# #679 Squirrel

Run Squirrel and print your greeting.

Canonical type `programming`, language_id `355`.

Suggested toolchain: Squirrel sq CLI original.

From the example directory:

```sh
sq hello.nut
```

Expected result: stdout Hello, World! and newline.

The runtime sq must be Squirrel, not another tool with the same name.

Recorded status: syntax verified; behavior verified. Toolchain: Squirrel 3.2 original sources + native GNU C++ build. [Log](verification/result.json).

Sources:

- [Squirrel](http://www.squirrel-lang.org/squirreldoc/reference/language.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.nut` | [hello.nut](hello.nut) verified |
