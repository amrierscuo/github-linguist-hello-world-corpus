# 0636: SQL: `.ddl`

SQL DDL SQLite con tabella e dato originale.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.ddl`.

Control provided, from the folder of the variant:

```text
sqlite3 :memory: < hello.ddl
```

Expected result: Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.sqlite.org/lang_select.html](https://www.sqlite.org/lang_select.html)
