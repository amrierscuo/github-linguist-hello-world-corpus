# 0520: PLSQL: `.prc`

Ruolo: Procedura stored PL/SQL con DBMS_OUTPUT.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Oracle Database e SQL*Plus. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
SQL*Plus di test: SET SERVEROUTPUT ON; @hello.prc; EXEC corpus_hello
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.prc`: `387a6fe5d402fcf975bcd53afd3f1c41aeb9aaf50bc576690703ba67afa9f8e9`

Primary sources:

- https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/plsql-subprograms.html
- https://docs.oracle.com/en/database/oracle/oracle-database/23/arpls/DBMS_OUTPUT.html
