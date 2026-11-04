# #369 LOLCODE

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Interpretare LOLCODE1.2 e stampare Hello, World!.

The program declares two variables, uses SMOOSH for concatenation and VISIBLE for output.

## Toolchain and reproduction

lci0.11.2 originale justinmeza, branch future; GCC e librerie readline/ncurses

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
lci hello.lol
```

## Expected result and status

stdout esattamente Hello, World! seguito da newline; exit0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://lolcode.org/
- https://github.com/justinmeza/lci

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.lol` | [hello.lol](hello.lol) verified |
