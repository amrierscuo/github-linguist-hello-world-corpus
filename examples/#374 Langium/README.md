# #374 Langium

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Generate a parser from a Langium grammar and recognize Hello, World!.

The grammar defines entry Model, ID and hidden whitespace. createServicesForGrammar analyzes the source and builds the original parser; the Hello, World! fixture is actually analyzed.

## Toolchain and reproduction

Langium4.4.0 /Chevrotain, Node22.20; actual version in the log

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
node verify.mjs
```

## Expected result and status

Nessun lexer/parser error; AST Model con audience=World.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://langium.org/docs/reference/grammar-language/
- https://github.com/eclipse-langium/langium

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.langium` | [hello.langium](hello.langium) verified |
