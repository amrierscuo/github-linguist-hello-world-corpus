# #796 YAML

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Analizzare YAML e leggere la stringa Hello, World!.

The safe loader interprets an original YAML mapping; the driver controls the scalar value.

## Toolchain and reproduction

PyYAML6.0.3 originale

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
python verify.py
```

## Expected result and status

Mapping con greeting = Hello, World!.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://pyyaml.org/wiki/PyYAMLDocumentation

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.yml` | [hello.yml](hello.yml) verified |
| `.mir` | [hello.mir](variants/mir-c4950490/hello.mir) verified |
| `.reek` | [hello.reek](variants/reek-d43e4b53/hello.reek) created; verification pending |
| `.rviz` | [hello.rviz](variants/rviz-2327f1f4/hello.rviz) created; verification pending |
| `.sublime-syntax` | [hello.sublime-syntax](variants/sublime-syntax-35002c21/hello.sublime-syntax) created; verification pending |
| `.syntax` | [hello.syntax](variants/syntax-0ed79f06/hello.syntax) created; verification pending |
| `.yaml` | [hello.yaml](variants/yaml-fa1b82e8/hello.yaml) created; verification pending |
| `.yaml-tmlanguage` | [hello.yaml-tmlanguage](variants/yaml-tmlanguage-f2fa8d15/hello.yaml-tmlanguage) created; verification pending |
| `.yaml.sed` | [hello.yaml.sed](variants/yaml-sed-463fad60/hello.yaml.sed) created; verification pending |
| `.yml.mysql` | [hello.yml.mysql](variants/yml-mysql-d412fc04/hello.yml.mysql) created; verification pending |
