# 0520: PLSQL: `.ddl`

Role: Script DDL with private test table and greeting default.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Oracle Database e SQL*Plus. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Oracle DB schema temporaneo isolato: @hello.ddl; leggere default nel dictionary; eliminare schema di test
```

Expected result: Default message = Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.ddl`: `bba0aa465e33298bbd0c860af4dfde16757d151f074cbfac49c2e410585a0388`

Primary sources:

- https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-TABLE.html
- https://docs.oracle.com/en/database/oracle/oracle-database/23/arpls/DBMS_OUTPUT.html
