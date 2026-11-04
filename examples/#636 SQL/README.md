# #636 SQL

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Execute SQL and return greeting Hello, World!.

Dialetto SQLite dichiarato; SELECT viene realmente analizzato ed eseguito su database in memoria.

## Toolchain and reproduction

Original SQLite3 via standard Python library sqlite3; log version

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
python verify.py
```

## Expected result and status

A row, column greeting, Hello, World! value.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://www.sqlite.org/lang_select.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.sql` | [hello.sql](hello.sql) verified |
| `.ddl` | [hello.ddl](variants/ddl-8bc7bf69/hello.ddl) created; verification pending |
| `.inc` | [hello.inc](variants/inc-dd126fb7/hello.inc) created; verification pending |
| `.mysql` | [hello.mysql](variants/mysql-94d2dcda/hello.mysql) created; verification pending |
| `.prc` | [hello.prc](variants/prc-8feafefc/hello.prc) created; verification pending |
| `.tab` | [hello.tab](variants/tab-97c85d6e/hello.tab) created; verification pending |
| `.udf` | [hello.udf](variants/udf-94d3d68a/hello.udf) created; verification pending |
| `.viw` | [hello.viw](variants/viw-71592285/hello.viw) created; verification pending |
