# #473 Ninja

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Run a Ninja graph that generates a file with Hello, World!.

The .ninja file defines rule, explicit dependence and default target. Original Ninja interprets the graph and starts the Python fixture; the content of the product file is compared exactly.

## Toolchain and reproduction

Ninja1.11.1, Python3 fixture

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
ninja -f hello.ninja
```

## Expected result and status

greeting.txt contains i13byte Hello, World!; exit0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://ninja-build.org/manual.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ninja` | [hello.ninja](hello.ninja) verified |
