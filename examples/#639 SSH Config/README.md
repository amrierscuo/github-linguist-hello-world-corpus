# #639 SSH Config

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Analyze SSH Config and evaluate the GREETING = Hello, World! option.

-G prints the actual configuration without opening connections. The file remains a local fixture; the illustrative host name uses example.invalid.

## Toolchain and reproduction

OpenSSH9.6p1 originale

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
ssh -G -F ssh-config hello-world
```

## Expected result and status

hostname hello-world.example.invalid e setenv GREETING=Hello, World!.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://man.openbsd.org/ssh_config
