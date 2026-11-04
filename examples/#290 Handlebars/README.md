# #290 Handlebars

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Fill in and make a Handlebars template with audience=World.

The original Handlebars compiler interprets {{audience}} in strict mode. The fixture provides the context and controls the product markup; the dependencies are isolated in work and the log keeps posters and lockfile NPM.

## Toolchain and reproduction

Handlebars4.7.8, Node.js22.20.0

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
node render.js
```

## Expected result and status

stdout <p>Hello, World!</p> seguito da newline; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://handlebarsjs.com/guide/

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.handlebars` | [hello.handlebars](variants/handlebars-d5d95d20/hello.handlebars) created; verification pending |
| `.hbs` | [hello.hbs](hello.hbs) verified |
