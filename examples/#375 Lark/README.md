# #375 Lark

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Build a parser LALR Lark and recognize Hello, World!.

The original Lark engine interprets hello.lark and builds the LALR parser. The tree tokens are compared with the Python fixture; the driver does not implement a replacement parser.

## Toolchain and reproduction

Lark1.3.1, CPython3.13.9

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
python verify.py
```

## Expected result and status

Albero start con token Hello e World; exit0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://lark-parser.readthedocs.io/en/latest/grammar.html
- https://github.com/lark-parser/lark

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.lark` | [hello.lark](hello.lark) verified |
