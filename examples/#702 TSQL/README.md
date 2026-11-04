# #702 TSQL

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Eseguire TSQL e restituire Hello, World! da SELECT.

The Unicode nvarchar variable is chained with the operator + of the TSQL dialect.

## Toolchain and reproduction

Microsoft SQL Server TSQL, versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
sqlcmd -i hello.sql
```

## Expected result and status

A line, greeting = Hello, World!.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Commitments: SQL Server/sqlcmd not available; parser and hanging execution.

## Primary sources

- https://learn.microsoft.com/en-us/sql/t-sql/language-elements/string-operators-transact-sql?view=sql-server-2017

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.sql` | [hello.sql](hello.sql) created; verification pending |
