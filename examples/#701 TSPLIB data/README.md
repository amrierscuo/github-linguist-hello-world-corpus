# #701 TSPLIB data

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Analyze an original TSP problem and read the Hello, World! metadata.

Three cities, distances EUC_2D and COMMENT containing greeting. The driver uses the authentic parser, controls the knots and a distance, then reads COMMENT; does not solve a TSP.

## Toolchain and reproduction

tsplib95 0.7.1 originale

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
python verify.py
```

## Expected result and status

COMMENT = Hello, World!, tre nodi e distanza1 fra nodi1 e2.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://tsplib95.readthedocs.io/en/stable/pages/usage.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.tsp` | [hello.tsp](hello.tsp) verified |
