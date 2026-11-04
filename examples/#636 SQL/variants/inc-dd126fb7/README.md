# 0636: SQL: `.inc`

Includeable Fragment SQL which retains the original query.

Origin: copy of the original `examples/#636 SQL/hello.sql` file.

Artefatto principale: `hello.inc`.

Control provided, from the folder of the variant:

```text
sqlite3 :memory: < hello.inc
```

Expected result: A line, greeting column, Hello, World! value..

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.sqlite.org/lang_select.html](https://www.sqlite.org/lang_select.html)
