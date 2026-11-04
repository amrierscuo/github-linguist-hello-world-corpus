# 0682: Starlark: `.bzl`

Chargeable Starlark module that returns greeting.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.bzl`.

Control provided, from the folder of the variant:

```text
Bazel/Starlark load("//:hello.bzl", "greeting"); print(greeting())
```

Expected result: Hello, World! value.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://bazel.build/rules/language](https://bazel.build/rules/language)
