# 0520: PLSQL: `.bdy`

Ruolo: Corpo package PL/SQL con implementazione; specifica separata.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Oracle Database e SQL*Plus. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
SQL*Plus di test: @spec.sql; @hello.bdy; SELECT corpus_greeting.greeting FROM dual
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.bdy`: `f6a36a006932ec10430d11941fbe58c44dfe97ad99ceca59d5157e010e2f1e3d`
- `spec.sql`: `9e49e46c4d7bf9942c9bdbe3e271b7d1ca0c148a21a228b2dfce95fd81d05ff1`

Primary sources:

- https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/plsql-packages.html
- https://docs.oracle.com/en/database/oracle/oracle-database/23/arpls/DBMS_OUTPUT.html
