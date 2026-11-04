# #236 Gemini

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Analyze a Gemini document and get the Hello, World! paragraph.

The original Gemtext library returns Heading/Paragraph types; verify.py compares the analyzed strings. No Gemini server or network request is required.

## Toolchain and reproduction

gemtext 1.1.0, CPython 3.13.9

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
python verify.py
```

## Expected result and status

PASS: Gemini paragraph = Hello, World!; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://geminiprotocol.net/docs/gemtext.gmi
- https://geminiprotocol.net/docs/gemtext-specification.gmi
- https://github.com/davep/gemtext

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.gmi` | [hello.gmi](hello.gmi) verified |
