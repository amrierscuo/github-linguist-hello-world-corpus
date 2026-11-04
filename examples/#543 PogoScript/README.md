# #543 PogoScript

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Fill out PogoScript and print Hello, World!.

The original CLI Pogo compiles the .pogo file and performs it in Node. audience is a language variable, console.log is the IO of the JavaScript backend.

## Toolchain and reproduction

Pogo0.10.0 ufficiale, Node22.20.0

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
pogo hello.pogo
```

## Expected result and status

Hello, World! seguito da newline; exit0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://featurist.github.io/pogoscript/
- https://github.com/featurist/pogoscript

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pogo` | [hello.pogo](hello.pogo) verified |
