# #186 EdgeQL

Evaluate a EdgeQL query that returns a singleton type str containing Hello, World!.

Canonical type `programming`, language_id `925235833`.

Provided toolchain: Gel/EdgeDB server and CLI client compatible.

From the example directory:

```sh
gel query --file hello.edgeql
```

Expected result: together singleton {' Hello, World! '}.

The query is read-only and does not require an application scheme. A local Gel server is however necessary for actual verification.

Initial state: created; syntax and behavioral verification pending. native toolchain not yet performed: syntax and behavior verifications remain pending.

Sources of linguaggio/formato and original implementations:

- [EdgeQL — SELECT](https://docs.geldata.com/reference/edgeql/select)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.edgeql` | [hello.edgeql](hello.edgeql) created; verification pending |
| `.esdl` | [hello.esdl](variants/ext-esdl-2e6573646c/hello.esdl) created; verification pending |
