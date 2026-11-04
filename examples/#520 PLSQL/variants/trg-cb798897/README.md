# 0520: PLSQL: `.trg`

Role: Trigger PL/SQL test on a dedicated table; no real DB is modified in preparation.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Oracle Database e SQL*Plus. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Oracle schema temporaneo: creare corpus_events(message VARCHAR2(30)); @hello.trg; INSERT con valore null; SELECT message
```

Expected result: Row containing Hello, World! after trigger

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.trg`: `6cc616bc64aa4c04d9d3929b1a4145fe2ee63ec18908bb661cebb081e26f9ee8`

Primary sources:

- https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/plsql-triggers.html
- https://docs.oracle.com/en/database/oracle/oracle-database/23/arpls/DBMS_OUTPUT.html
