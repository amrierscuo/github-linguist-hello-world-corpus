# 0399: LookML: `.lookml`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#399 LookML/hello.view.lkml.

Required toolchain: Community lkml 1.3.7 genuine LookML parser; SQLite 3.51.0; Python 3.13.9. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.lookml; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: Parser accepts view/derived_table/dimension; SQL returns greeting; Looker must validate and question the size.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.lookml`: `59870c7955ce0f2e9462e464fc8a32eeeadca43bd96782da82e1b38ce43d262e`
- `requirements.txt`: `d74b32eaaf2c09fc4650a0d2d80fa9007320a4e288989534904bfe613a74ec7f`
- `verify.py`: `2c06ea75bec9133fc326974e2c7ab6c4031805d966b5be52c520d71884c32b79`

Primary sources:

- https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table
- https://github.com/joshtemple/lkml
