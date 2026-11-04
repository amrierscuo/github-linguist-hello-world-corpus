# #377 Latte

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Fill out and make a Latte template with audience=World.

The original Latte\Engine and renderToString. The driver loads the original files via PSR4 autoload; the template is analyzed and compiled by the Milk engine, not replaced manually.

## Toolchain and reproduction

Latte3.0.26, PHP8.3.6 con tokenizer

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
php render.php
```

## Expected result and status

stdout <p>Hello, World!</p> seguito da newline; exit0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://latte.nette.org/en/develop
- https://github.com/nette/latte/tree/v3.0.26

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.latte` | [hello.latte](hello.latte) verified |
