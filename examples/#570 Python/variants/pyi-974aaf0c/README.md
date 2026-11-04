# 0570: Python: `.pyi`

Type stub Python: describes the function, does not perform the body.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.pyi`.

Control provided, from the folder of the variant:

```text
mypy main.py --strict
```

Expected result: accepted interface and implementation returns greeting.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://typing.python.org/en/latest/spec/distributing.html#stub-files](https://typing.python.org/en/latest/spec/distributing.html#stub-files)
