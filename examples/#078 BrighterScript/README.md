# #078 BrighterScript

Canonical entry from the corpus's `reference/languages.yml`. The reference and its order remain unchanged. The source was written for this example.

## Goal

Validate and transpire a BrighterScript namespace, then run the generated BrightScript.

Corpus.greeting returns the string; main printing. bsconfig.json configures the local staging and disables the creation of a package. behavior was verified with brs out of a Roku device.

## Toolchain and reproduction

BrighterScript 0.73.5; brs 0.45.0; Node.js 22.20.0

Command from the example folder, with the toolchain indicated available in the PATH. Run the build in a temporary copy to keep the generated files out of the corpus.

```text
bsc --project bsconfig.json
```

```text
brs stage/source/main.brs
```

## Expected result and status

Validation without errors; exact stdout Hello, World! followed by newline; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records actual commands, versioni/provenienza of the toolchain, output codes, stdout/stderr and SHA-256 of the proven sources.

## Primary sources

- https://github.com/rokucommunity/brighterscript
- https://github.com/rokucommunity/brighterscript/blob/master/docs/bsconfig.md
- https://github.com/sjbarag/brs

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.bs` | [main.bs](source/main.bs) verified |
