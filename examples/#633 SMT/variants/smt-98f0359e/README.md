# 0633: SMT: `.smt`

Textual variation of the same format, with canon suffix .smt.

Origin: copy of the original `examples/#633 SMT/hello.smt2` file.

Artefatto principale: `hello.smt`.

Control provided, from the folder of the variant:

```text
z3 -smt2 hello.smt
```

Expected result: sat e (greeting "Hello, World!" )..

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://smt-lib.org/theories-UnicodeStrings.shtml](https://smt-lib.org/theories-UnicodeStrings.shtml)
