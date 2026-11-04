# #751 Vespa Schema Definition

Validate a Vespa scheme and save a message field readable by summary.

Canonical type `data`, language_id `587879709`.

Suggested toolchain: Vespa application validator and test server.

From the example directory:

```sh
Validare hello.sd in un application package e caricare document.json in un’istanza isolata.
```

Expected result: accepted scheme; document summary returns message Hello, World!.

The contract and the document are original. The complete validation requires the Vespa model.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [Vespa schema reference](https://docs.vespa.ai/en/reference/schema-reference.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.sd` | [hello.sd](hello.sd) created; verification pending |
