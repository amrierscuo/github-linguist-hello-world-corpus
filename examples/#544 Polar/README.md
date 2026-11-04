# #544 Polar

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Upload a Polar rule and get binding= Hello, World!.

The greeting rule is an original Polar fact. Oso loads the policy and the driver questions the engine with Variable(message), comparing the binding value. It is not an authorization policy applied to resources; the Oso notice for absence of allow is recorded.

## Toolchain and reproduction

Oso/Polar0.27.3, CFFI1.17.1, Python3.12 Linux

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
python3 verify.py
```

## Expected result and status

A message= Hello, World! solution, issued by the driver; exit0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://github.com/osohq/oso
- https://docs.oso.dev/ruby/getting-started/application/model.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.polar` | [hello.polar](hello.polar) verified |
