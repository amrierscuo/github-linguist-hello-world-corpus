# #283 HTML+ERB

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Render HTML + ERB with a Ruby binding that provides audience=World.

ERB.new reads the template, result(binding) evaluates the Ruby interpolation. The original driver compares the document produced by the ERB engine; does not build the HTML by manual replacements.

## Toolchain and reproduction

Ruby3.2.3, ERB of standard library

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
ruby render.rb
```

## Expected result and status

stdout <p>Hello, World!</p> seguito da newline; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://docs.ruby-lang.org/en/3.2/ERB.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.erb` | [hello.erb](hello.erb), [fixture.html.erb](variants/erb-deface-ad7ccb60/fixture.html.erb) created; verification pending |
| `.erb.deface` | [hello.html.erb.deface](variants/erb-deface-ad7ccb60/hello.html.erb.deface) created; verification pending |
| `.rhtml` | [hello.rhtml](variants/rhtml-6f031adf/hello.rhtml) created; verification pending |
