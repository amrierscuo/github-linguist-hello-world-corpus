# #363 Koka

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Fill in Koka and print Hello, World!.

main uses val and the ++ concatenation operator. The original compiler parses and checks types, then compiles and links the C output. The binary runs only in the work directory.

## Toolchain and reproduction

Koka3.2.9, backend C e GCC

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
koka -o hello hello.kk
```

```text
./hello
```

## Expected result and status

stdout esattamente Hello, World! seguito da newline; exit0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://koka-lang.github.io/koka/doc/book.html
- https://github.com/koka-lang/koka/releases/tag/v3.2.9

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.kk` | [hello.kk](hello.kk) verified |
