# 0593: RPGLE: `.sqlrpgle`

RPG free form con embedded SQL; necessita SQL precompiler IBM i.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.sqlrpgle`.

Control provided, from the folder of the variant:

```text
IBM i CRTSQLRPGI OBJ(TESTLIB/HELLO) SRCSTMF(hello.sqlrpgle); CALL TESTLIB/HELLO
```

Expected result: Hello, World! display.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.ibm.com/docs/en/i/7.5.0?topic=applications-coding-sql-statements-in-ile-rpg](https://www.ibm.com/docs/en/i/7.5.0?topic=applications-coding-sql-statements-in-ile-rpg)
