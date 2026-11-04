# 0636: SQL: `.tab`

## Latest recorded verification

**Syntax and behavior verified** for `.tab`. Native SQLite engine through CPython sqlite3, using a new in-memory database; execute every SQL statement in the exact file and assert its only result set. [Recorded evidence](../../verification/native_20261104_followup_2e746162.json).

Definizione SQL di tabella con default originale.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.tab`.

Control provided, from the folder of the variant:

```text
sqlite3 :memory: < hello.tab
```

Expected result: Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.sqlite.org/lang_select.html](https://www.sqlite.org/lang_select.html)
