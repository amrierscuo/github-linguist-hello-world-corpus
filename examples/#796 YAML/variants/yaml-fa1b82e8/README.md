# 0796: YAML: `.yaml`

YAML document of the same format; .yaml composite suffix preserved exactly. The template is static and does not declare replacements or a specific MySQL configuration.

Origin: copy of the original `examples/#796 YAML/hello.yml` file.

Artefatto principale: `hello.yaml`.

Control provided, from the folder of the variant:

```text
Python yaml.safe_load: parse hello.yaml; assert greeting == "Hello, World!"
```

Expected result: Mapping with greeting = Hello, World!..

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://pyyaml.org/wiki/PyYAMLDocumentation](https://pyyaml.org/wiki/PyYAMLDocumentation)
