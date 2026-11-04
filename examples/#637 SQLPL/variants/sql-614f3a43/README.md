# 0637: SQLPL: `.sql`

Textual variation of the same format, with canon suffix .sql.

Origin: copy of the original `examples/#637 SQLPL/hello.db2` file.

Artefatto principale: `hello.sql`.

Control provided, from the folder of the variant:

```text
db2 -td@ -vf hello.sql
```

Expected result: The OUT greeting parameter is worth Hello, World! after CALL corpus_greeting(?).

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.ibm.com/docs/en/db2-for-zos/12.0.0?topic=procedures-sql-procedure-body](https://www.ibm.com/docs/en/db2-for-zos/12.0.0?topic=procedures-sql-procedure-body)
