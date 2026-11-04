# #406 M4Sugar

Use M4Sugar with quad odds, initialization and diversions to expand greeting.

Canonical type `programming`, language_id `216`.

Suggested toolchain: GNU Autoconf autom4te with M4sugar language.

From the example directory:

```sh
autom4te --language=M4sugar --no-cache hello.m4
```

Expected result: Hello, World! greeting in output; only spazi/fine external line is allowed.

M4 simple does not automatically charge M4Sugar: the command uses autom4te and the appropriate language.

Recorded status: syntax verified; behavior verified. Toolchain: GNU Autoconf autom4te + M4Sugar (local extracted packages). [Log](verification/result.json).

Sources:

- [GNU Autoconf — M4Sugar](https://www.gnu.org/software/autoconf/manual/autoconf-2.72/html_node/M4sugar.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.m4` | [hello.m4](hello.m4) verified |
