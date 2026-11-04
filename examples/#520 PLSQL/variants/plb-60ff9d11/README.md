# 0520: PLSQL: `.plb`

Role: Variant with ruolo/formato distinct from the main source.

Provenience: Only block documentation; no artifact with required extension was manufactured.

Required toolchain: Oracle Database e SQL*Plus. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Disponibilità del tool originale necessaria; consultare gli impedimenti.
```

Expected result: To check with the native format after the block resolution.

Individual status: artifact created `false`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- Output of the PL/SQL wrap utility, not ordinary text source. The original Oracle wrapper is not available: no wrapped sequence is manufactured.

Primary sources:

- https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/wrapping-pl-sql-source-text-pl-sql-wrapper-utility.html
- https://docs.oracle.com/en/database/oracle/oracle-database/23/arpls/DBMS_OUTPUT.html
