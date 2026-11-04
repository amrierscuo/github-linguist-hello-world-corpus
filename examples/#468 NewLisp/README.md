# #468 NewLisp

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Interpretare newLISP e stampare Hello, World!.

set alloy audience; string builds greeting, println realizes the IO and exit0 ends the program.

## Toolchain and reproduction

newLISP10.7.5 Linux ufficiale Ubuntu

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
newlisp hello.nl
```

## Expected result and status

Hello, World! seguito da newline; exit0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://www.newlisp.org/downloads/newlisp_manual.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.nl` | [hello.nl](hello.nl) verified |
| `.lisp` | [hello.lisp](variants/lisp-757ceb1b/hello.lisp) created; verification pending |
| `.lsp` | [hello.lsp](variants/lsp-270be2e4/hello.lsp) created; verification pending |
