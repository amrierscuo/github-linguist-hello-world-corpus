# #558 Prolog

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Interpret Prolog and solve main printing Hello, World!.

initialization(main,main) defines the program startup. Atomic_list_concat builds the value and writeln issues it in the original Prolog runtime.

## Toolchain and reproduction

SWI-Prolog9.0.4 ufficiale Ubuntu

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
swipl -q hello.pl
```

## Expected result and status

Hello, World! seguito da newline; exit0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://www.swi-prolog.org/pldoc/doc_for?object=atomic_list_concat/2
- https://www.swi-prolog.org/pldoc/doc_for?object=initialization/2

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pl` | [hello.pl](hello.pl) verified |
| `.plt` | [hello.plt](variants/plt-cc71c907/hello.plt) created; verification pending |
| `.pro` | [hello.pro](variants/pro-1d8a87ac/hello.pro) created; verification pending |
| `.prolog` | [hello.prolog](variants/prolog-26531ed3/hello.prolog) created; verification pending |
| `.yap` | [hello.yap](variants/yap-42bad85d/hello.yap) created; verification pending |
