# 0636: SQL: `.udf`

UDF scale T- SQL for SQL Server in test database.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.udf`.

Control provided, from the folder of the variant:

```text
sqlcmd -i hello.udf (isolated test database)
```

Expected result: Hello, World! return function.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://learn.microsoft.com/en-us/sql/t-sql/statements/create-function-transact-sql](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-function-transact-sql)
