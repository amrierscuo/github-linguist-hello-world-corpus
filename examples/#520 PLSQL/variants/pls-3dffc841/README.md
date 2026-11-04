# 0520: PLSQL: `.pls`

Role: Anonymous block PL/SQL without SET client directives; same SQL procedural language.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Oracle Database e SQL*Plus. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
SQL*Plus di test: SET SERVEROUTPUT ON; @hello.pls
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.pls`: `964f21462fc46b2baa6d32ce9273cfee5c17434b080cdf0be23fd1fdfd402459`

Primary sources:

- https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/overview.html
- https://docs.oracle.com/en/database/oracle/oracle-database/23/arpls/DBMS_OUTPUT.html
