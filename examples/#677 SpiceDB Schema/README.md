# #677 SpiceDB Schema

Validate a SpiceDB scheme and a caveat that allows reading message is greeting.

Canonical type `data`, language_id `864005057`.

Suggested toolchain: SpiceDB and zed in isolated environment.

From the example directory:

```sh
zed validate hello.zed; valutare la caveat greeting in un backend SpiceDB isolato con message="Hello, World!".
```

Expected result: accepted scheme; caveat greeting true only for Hello, World!.

The example does not change a permission database. The exact command depends on the zed version.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [SpiceDB schema](https://authzed.com/docs/spicedb/concepts/schema)
- [SpiceDB caveats](https://authzed.com/docs/spicedb/concepts/caveats)

zed validated also accepts raw .zed files; the control of the caveat in a backend remains a distinct requirement. [CLI originale](https://github.com/authzed/zed/blob/main/internal/cmd/validate.go).

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.zed` | [hello.zed](hello.zed) created; verification pending |
