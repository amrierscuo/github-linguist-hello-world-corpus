# #463 Nearley

## Latest recorded verification

Latest extension checks:
- `.nearley`: Nearley original compiler emits a parser from this grammar file; the parser recognizes the exact greeting. [Evidence](verification/native_20261104_followup_2e6e6561726c6579.json).

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Fill in a Nearley grammar and recognize Hello, World!.

The nearleyc compiler generates the parser from the original grammar; the driver feeds the Nearley parser with greeting and compares the only result. hello.js is generated only in the copy in work.

## Toolchain and reproduction

Nearley2.20.1, Node22.20.0

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
nearleyc hello.ne -o hello.js
```

```text
node verify.js
```

## Expected result and status

Hello, World! seguito da newline; exit0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://nearley.js.org/docs/grammar
- https://nearley.js.org/docs/parser

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ne` | [hello.ne](hello.ne) verified |
| `.nearley` | [hello.nearley](variants/nearley-659604fb/hello.nearley) syntax and behavior verified |