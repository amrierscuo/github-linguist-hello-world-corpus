# 0607: Red: `.reds`

Red/System program with FFI Linux libc, distinct from the Red standard library.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.reds`.

Control provided, from the folder of the variant:

```text
red -r hello.reds -o work/hello; work/hello
```

Expected result: Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://static.red-lang.org/red-system-specs.html](https://static.red-lang.org/red-system-specs.html)
