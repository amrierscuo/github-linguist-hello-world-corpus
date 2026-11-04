# 0636: SQL: `.mysql`

Query MySQL; the CONCAT function requires the appropriate dialect.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.mysql`.

Control provided, from the folder of the variant:

```text
mysql --batch --skip-column-names < hello.mysql
```

Expected result: Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://dev.mysql.com/doc/refman/8.4/en/string-functions.html#function_concat](https://dev.mysql.com/doc/refman/8.4/en/string-functions.html#function_concat)
