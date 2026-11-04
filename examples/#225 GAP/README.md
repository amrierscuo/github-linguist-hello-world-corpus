# #225 GAP

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Evaluate a GAP expression, print it and finish successfully.

Concatenation builds greeting, Print produces greeting and QUIT_GAP (0) concludes the process. The verification executes the authentic GAP track with the isolated basic library and without optional package.

## Toolchain and reproduction

GAP 4.12.1, pacchetti Ubuntu 4.12.1-2build2

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
gap -q -A -T hello.g
```

## Expected result and status

stdout esattamente Hello, World! seguito da newline; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://docs.gap-system.org/doc/tut/manual.pdf
- https://www.gap-system.org/

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.g` | [hello.g](hello.g), [consumer.g](variants/ext-gd-2e6764/consumer.g), [consumer.g](variants/ext-gi-2e6769/consumer.g) created; verification pending |
| `.gap` | [hello.gap](variants/ext-gap-2e676170/hello.gap) created; verification pending |
| `.gd` | [hello.gd](variants/ext-gd-2e6764/hello.gd) created; verification pending |
| `.gi` | [hello.gi](variants/ext-gi-2e6769/hello.gi) created; verification pending |
| `.tst` | [hello.tst](variants/ext-tst-2e747374/hello.tst) created; verification pending |
