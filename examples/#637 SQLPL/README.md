# #637 SQLPL

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Create a SQL PL procedure that returns Hello, World! to a OUT parameter.

The @ terminator distinguishes the end of the body from its points and commas. The greeting is assigned to the OUT parameter; it serves a subsequent call to read it.

## Toolchain and reproduction

IBM Db2 SQL PL, versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
db2 -td@ -vf hello.db2
```

## Expected result and status

The OUT greeting parameter applies Hello, World! after CALL corpus_greeting(?).

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Commitments: unavailable test Db2; creazione/chiamata and hanging parser.

## Primary sources

- https://www.ibm.com/docs/en/db2-for-zos/12.0.0?topic=procedures-sql-procedure-body

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.sql` | [hello.sql](variants/sql-614f3a43/hello.sql) created; verification pending |
| `.db2` | [hello.db2](hello.db2) created; verification pending |
