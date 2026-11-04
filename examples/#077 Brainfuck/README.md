# #077 Brainfuck

Canonical entry from the corpus's `reference/languages.yml`. The reference and its order remain unchanged. The source was written for this example.

## Goal

Run an original Brainfuck program that issues Hello, World! and newline.

The program uses a cell and arithmetic variations between the ASCII codes later. The verification uses the native parser and interpreter of the upstream project; it does not use a written interpreter for this corpus.

## Toolchain and reproduction

fabianishere/brainfuck 2.7.3, interprete C originale compilato con GNU C

Command from the example folder, with the toolchain indicated available in the PATH. Run the build in a temporary copy to keep the generated files out of the corpus.

```text
Compilare l’interprete upstream con la dipendenza opzionale editline disabilitata.
```

```text
brainfuck hello.bf
```

## Expected result and status

stdout esatto Hello, World! seguito da newline; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records actual commands, versioni/provenienza of the toolchain, output codes, stdout/stderr and SHA-256 of the proven sources.

## Primary sources

- https://github.com/fabianishere/brainfuck

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.b` | [hello.b](variants/ext-b-2e62/hello.b) created; verification pending |
| `.bf` | [hello.bf](hello.bf) verified |
