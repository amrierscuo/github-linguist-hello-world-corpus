# #281 HTML+ECR

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Render a HTML + ECR template with World audience and produce the Hello, World! paragraph.

ECR.render incorporates the template into the Crystal program during compilation. audience is a value of the Crystal context interpolated in the HTML.

## Toolchain and reproduction

Crystal 1.11.2, LLVM17.0.6, ECR stdlib; GNU linker e PCRE8.39 isolata

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
crystal build render.cr -o render
```

```text
./render
```

## Expected result and status

stdout <p>Hello, World!</p> seguito da newline; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://crystal-lang.org/api/1.11.2/ECR.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ecr` | [hello.ecr](hello.ecr) verified |
