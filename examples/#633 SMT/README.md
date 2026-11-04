# #633 SMT

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Solve a string bond and read Hello, World! from the SMT model.

SMT - LIB2 uses string theory and str.++; Z3 produces sats and the value of the greeting variable.

## Toolchain and reproduction

Z3 solver5.1.0 originale

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
z3 hello.smt2
```

## Expected result and status

sat e ((greeting "Hello, World!")).

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://smt-lib.org/theories-UnicodeStrings.shtml

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.smt2` | [hello.smt2](hello.smt2) verified |
| `.smt` | [hello.smt](variants/smt-98f0359e/hello.smt) created; verification pending |
| `.z3` | [hello.z3](variants/z3-f29d6e3b/hello.z3) created; verification pending |
