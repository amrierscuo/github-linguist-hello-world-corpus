# #299 Hy

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Fill in and run Hy to print Hello, World!.

The form setv alloy greeting to the result of the prefixed concatenation; print uses the builtin Python from the Hy language. Verification passes through the authentic CLI/compiler Hy and the resulting VM Python.

## Toolchain and reproduction

Hy1.3.1, funcparserlib1.0.1, CPython3.13.9

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
hy hello.hy
```

## Expected result and status

stdout esattamente Hello, World! seguito da newline; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://hylang.org/hy/doc/v1.1.0/tutorial
- https://github.com/hylang/hy

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.hy` | [hello.hy](hello.hy) verified |
