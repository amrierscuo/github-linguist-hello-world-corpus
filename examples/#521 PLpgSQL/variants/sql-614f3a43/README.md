# 0521: PLpgSQL: `.sql`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#521 PLpgSQL/hello.pgsql.

Required toolchain: Authentic PostgreSQL PL/pgSQL engine, psql (PostgreSQL) 16.15 (Ubuntu 16.15-0ubuntu0.24.04.1). The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.sql; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: The conformed result contains Hello, World!, according to the framework described.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.sql`: `9e12a294843a6e9e7e44b92a6d9f4cc29d173f9338b49929cb17374770e92851`

Primary sources:

- https://www.postgresql.org/docs/16/plpgsql.html
