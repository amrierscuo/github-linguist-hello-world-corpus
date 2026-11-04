# #471 Nickel

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Evaluate Nickel and get the field greeting= Hello, World!.

the original evaluator exports the JSON record, compared with the expected value.

## Toolchain and reproduction

Nickel1.18.0 ufficiale Windows

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
nickel export --format json hello.ncl
```

## Expected result and status

JSON {"greeting":"Hello, World!"}; exit0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://nickel-lang.org/user-manual/tutorial/
- https://github.com/tweag/nickel/releases/tag/1.18.0

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ncl` | [hello.ncl](hello.ncl) verified |
