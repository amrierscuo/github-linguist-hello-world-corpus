# #630 SCSS

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Fill in SCSS and get a CSS content value equal to Hello, World!.

The Sass compiler evaluates interpolation in the string; the test involves the CSS generated and not a browser.

## Toolchain and reproduction

Dart Sass1.105.1 originale, Node22.20.0

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
sass hello.scss
```

## Expected result and status

CSS contains content: "Hello, World!".

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://sass-lang.com/documentation/interpolation/

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.scss` | [hello.scss](hello.scss) verified |
