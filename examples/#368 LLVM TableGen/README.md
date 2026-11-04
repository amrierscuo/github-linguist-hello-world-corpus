# #368 LLVM TableGen

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Evaluate a LLVM TableGen record and get Text= Hello, World!.

The Greeting class receives audiences,!strconcat builds value and def Hello specializes World. The goal is a record evaluated by the true TableGen, without simulating a machine architecture.

## Toolchain and reproduction

LLVM TableGen18.1.3

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
llvm-tblgen hello.td -print-records
```

## Expected result and status

The record def Hello contains text string = "Hello, World!"; exit0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://llvm.org/docs/TableGen/ProgRef.html
- https://llvm.org/docs/CommandGuide/tblgen.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.td` | [hello.td](hello.td) verified |
