# #710 Tcsh

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Eseguire Tcsh e stampare Hello, World!.

The script uses set and expansion of the variable; -f disables personal boot files.

## Toolchain and reproduction

Tcsh6.24.10 originale

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
tcsh -f hello.tcsh
```

## Expected result and status

Hello, World! su stdout.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://www.tcsh.org/

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.tcsh` | [hello.tcsh](hello.tcsh) verified |
| `.csh` | [hello.csh](variants/csh-6f61e238/hello.csh) created; verification pending |
