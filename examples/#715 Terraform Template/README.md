# #715 Terraform Template

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Evaluate a Terraform Template with audience = World.

templatefile really interprets .tftpl file and variable. The test does not use provider, infrastructure, init, remote status or network.

## Toolchain and reproduction

Terraform1.16.5 ufficiale

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
terraform console < evaluate.txt
```

## Expected result and status

String value Hello, World! followed by newline; console can use heredoc notation.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://developer.hashicorp.com/terraform/language/functions/templatefile

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.tftpl` | [hello.tftpl](hello.tftpl) verified |
