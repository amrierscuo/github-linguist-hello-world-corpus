# #559 Promela

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Simulate a process init Promela and print Hello, World!.

The model uses init and printf. Spin original analyzes and performs the model in the local simulation; the test does not attribute properties of model checking further to greeting.

## Toolchain and reproduction

Spin6.5.2 ufficiale Ubuntu

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
spin -T hello.pml
```

## Expected result and status

Simulation emits Hello, World!; a created process; exit0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://spinroot.com/spin/Man/printf.html
- https://spinroot.com/spin/Man/promela.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pml` | [hello.pml](hello.pml) verified |
