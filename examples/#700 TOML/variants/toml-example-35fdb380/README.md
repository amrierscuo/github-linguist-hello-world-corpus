# 0700: TOML: `.toml.example`

Textual variation of the same format, with canon suffix .toml.example.

Origin: copy of the original `examples/#700 TOML/hello.toml` file.

Artefatto principale: `hello.toml.example`.

Control provided, from the folder of the variant:

```text
Python tomllib: parse hello.toml.example, assert greeting == "Hello, World!"
```

Expected result: Hello, World! in the compliant result, according to the framework described..

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://toml.io/en/v1.0.0](https://toml.io/en/v1.0.0)
