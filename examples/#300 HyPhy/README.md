# #300 HyPhy

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Play a batch HyPhy HBL and print the greeting via fprintf(stdout,...).

The .bf file is HyPhy Batch Language, distinguished by Brainfuck. greeting is a string and fprintf expression emits the value. The program does not require genetic data, sequence analysis or statistical calculation; the log test the original runtime.

## Toolchain and reproduction

HyPhy2.5.59(MP), binario Linux x86SSE4 e pacchetti Ubuntu2.5.59+dfsg-1build3

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
hyphy hello.bf
```

## Expected result and status

stdout esattamente Hello, World! seguito da newline; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://hyphy.org/
- https://github.com/veg/hyphy
- https://raw.githubusercontent.com/veg/hyphy/master/tests/hbltests/RegressionTesting/LocalReferenceBug.bf

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.bf` | [hello.bf](hello.bf) verified |
