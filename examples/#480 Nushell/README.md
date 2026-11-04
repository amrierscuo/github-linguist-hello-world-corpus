# #480 Nushell

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Interpretare Nushell e stampare Hello, World!.

let alloy audience and the $ "..." interpolated string uses ($audience).The original performer is started without loading the personal configuration.

## Toolchain and reproduction

Nushell0.116.1 ufficiale Windows

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
nu --no-config-file hello.nu
```

## Expected result and status

Hello, World! seguito da newline; exit0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://www.nushell.sh/book/scripts.html
- https://github.com/nushell/nushell/releases/tag/0.116.1

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.nu` | [hello.nu](hello.nu) verified |
