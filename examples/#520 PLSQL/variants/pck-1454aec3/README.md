# 0520: PLSQL: `.pck`

Ruolo: Script package completo con specifica e corpo, distinto dai singoli file spec/body.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Oracle Database e SQL*Plus. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
SQL*Plus di test: @hello.pck; SELECT corpus_greeting.greeting FROM dual
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.pck`: `45a13a5f73eaa6f1bae49ee8151b5577934a9ab08d762e3d0efb4293438e76ff`

Primary sources:

- https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/plsql-packages.html
- https://docs.oracle.com/en/database/oracle/oracle-database/23/arpls/DBMS_OUTPUT.html
