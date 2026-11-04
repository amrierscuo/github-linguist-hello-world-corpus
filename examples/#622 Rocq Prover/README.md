# #622 Rocq Prover

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Define your greeting and check for a proof of equality, then evaluate it with Compute.

Native processing and Coq kernel control greeting_value; Compute evaluates concatenation. Coq8.18 is the actually executed version, not a Rocq9 runtime.

## Toolchain and reproduction

Coq8.18.0 original (language today called Rocq Prover)

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
coqc hello.v
```

## Expected result and status

Compute produces "Hello, World!": string and test compile.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://rocq-prover.org/doc/V8.19.2/refman/language/core/definitions.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.v` | [hello.v](hello.v) verified |
| `.coq` | [hello.coq](variants/coq-98f35b68/hello.coq) created; verification pending |
