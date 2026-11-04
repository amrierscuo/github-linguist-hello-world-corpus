# 0520: PLSQL: `.fnc`

Role: Stored PL/SQL function of greeting.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Oracle Database e SQL*Plus. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
SQL*Plus di test: @hello.fnc; SELECT corpus_greeting FROM dual
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.fnc`: `cf780ca738d44e7db6b6bf32a3939ad3895579089e5675843c65245eeea9b7c6`

Primary sources:

- https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/plsql-subprograms.html
- https://docs.oracle.com/en/database/oracle/oracle-database/23/arpls/DBMS_OUTPUT.html
