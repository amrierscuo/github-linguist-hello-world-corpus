# #289 Haml

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Render a Haml template that chains Hello, and World! into a paragraph.

%p defines the tag and = introduces the expression Ruby. Haml::Template is the original renderr; the fixed driver Haml6.3.0 for reproducibility and uses the recorded gems in the log, installed in work.

## Toolchain and reproduction

Haml6.3.0, Temple0.10.7, Tilt2.9.0, Thor1.5.0; Ruby3.2.3

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
ruby render.rb
```

## Expected result and status

stdout <p>Hello, World!</p> seguito da newline; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://haml.info/docs/yardoc/file.REFERENCE.html
- https://github.com/haml/haml
- https://rubygems.org/gems/haml/versions/6.3.0

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.haml` | [hello.haml](hello.haml) verified |
| `.haml.deface` | [hello.html.haml.deface](variants/haml-deface-a5c3691d/hello.html.haml.deface) created; verification pending |
