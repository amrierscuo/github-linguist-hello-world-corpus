# #478 NumPy

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Run a NumPy source and convert an uint8 array into the Hello, World! greeting.

The .numpy extension is canonical in Linguist. The program creates a real ndarray of13byte uint8, controls the shape and uses tobytes/decode; the test performs operations of the original NumPy library.

## Toolchain and reproduction

NumPy2.5.3, CPython3.13.9

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
python hello.numpy
```

## Expected result and status

Hello, World! seguito da newline; exit0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://numpy.org/doc/stable/reference/generated/numpy.array.html
- https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tobytes.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.numpy` | [hello.numpy](hello.numpy) verified |
| `.numpyw` | [hello.numpyw](variants/numpyw-c25621b9/hello.numpyw) created; verification pending |
| `.numsc` | [hello.numsc](variants/numsc-81e0ad98/hello.numsc) created; verification pending |
