# 0520: PLSQL: `.tps`

Role: Specify object type PL/SQL; method statement.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Oracle Database e SQL*Plus. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Oracle schema isolato: @hello.tps; @body.sql; SELECT corpus_greeting('World').greeting() FROM dual
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `body.sql`: `5db31c9025f7b67703917765657beb9a3bdcb0026b7914b1f5bc0abc2714881d`
- `hello.tps`: `46d2c6fc2d3679f20679adba899888e35f962b6b096af4014e456c64f3d2430f`

Primary sources:

- https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/overview-of-pl-sql-object-types.html
- https://docs.oracle.com/en/database/oracle/oracle-database/23/arpls/DBMS_OUTPUT.html
