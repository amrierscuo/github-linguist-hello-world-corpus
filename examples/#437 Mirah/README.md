# #437 Mirah

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
| `.mirah` | [hello.mirah](hello.mirah) created; verification pending |
