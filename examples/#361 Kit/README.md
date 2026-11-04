# #361 Kit

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Render a Kit template with variable audience and get the Hello, World! paragraph.

The directives are special comments Kit: assigning $audience and replacing the variable. Greeting does not depend on ordinary comments ignored by HTML.

## Toolchain and reproduction

CodeKit con compiler Kit originale; versione da registrare

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
Compilare hello.kit con CodeKit/Kit.
```

## Expected result and status

HTML contains <p> Hello, World! </p>.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no native parser/compilatore/runtime performed for this item.

Commitments: Original Compiler Kit written for Cocoa/macOS unavailable; maker not executed.

## Primary sources

- https://codekitapp.com/help/kit/index.html
- https://github.com/bdkjones/Kit

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.kit` | [hello.kit](hello.kit) created; verification pending |
