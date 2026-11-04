# #367 LLVM

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Assemble LLVM IR and perform main printing Hello, World! via puts.

The di14byte array includes NUL terminator. main calls puts with a LLVM pointer and returns0; llvm-as controls IR and types, lli executes code with native JIT.

## Toolchain and reproduction

LLVM18.1.3 Ubuntu, llvm-as e lli

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
llvm-as hello.ll -o hello.bc
```

```text
lli hello.bc
```

## Expected result and status

stdout esattamente Hello, World! seguito da newline; exit0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://llvm.org/docs/LangRef.html
- https://llvm.org/docs/CommandGuide/lli.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ll` | [hello.ll](hello.ll) verified |
