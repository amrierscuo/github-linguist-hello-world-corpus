# #634 SPARQL

## Latest recorded verification

Latest extension checks:
- `.sparql`: RDFlib SPARQL parser and query evaluator: one greeting binding. [Evidence](verification/native_20261104_followup_2e73706172716c.json).

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Evaluate a SPARQL query that chain Hello, and World!.

Query SPARQL1.1 on blank graph; the driver uses parser/evaluatore RDFlib and controls a single solution.

## Toolchain and reproduction

RDFlib7.6.0 originale

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
python verify.py
```

## Expected result and status

A single line with greeting = Hello, World!.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://www.w3.org/TR/sparql11-query/#func-concat

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.sparql` | [hello.sparql](variants/sparql-6c620153/hello.sparql) syntax and behavior verified |
| `.rq` | [hello.rq](hello.rq) verified |
