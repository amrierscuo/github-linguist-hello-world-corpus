# #142 Csound Document

The canonical entry and order come from the corpus's `reference/languages.yml`. Sources and fixtures are original; any dumps or bundles come from the stated tools.

## Goal

Run a full Csound document that includes options, orchestra and score.

hello.csd is the unified format with CsOptions, CsInstruments and CsScore. The runtime compiles the document and activates the tool. The -n -d -m0 options do not require audio or devices; the Csound message is registered on stderr. The warning directory plugin covers optional plugins.

## Toolchain and reproduction

Csound 6.18, pacchetto Ubuntu 6.18.1+dfsg-1ubuntu4 x86_64

Commands in the example folder with the toolchain available in PATH. Use a temporary copy: databases, objects, audio and other test outputs do not belong to the corpus.

```text
csound hello.csd
```

## Expected result and status

Messaggio Hello, World! seguito da newline; 0 errors in performance e exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records versions and provenance, SHA-256 of the source, actual commands, exit, stdout and stderr normalized.

## Primary sources

- https://csound.com/docs/manual/CommandUnifile.html
- https://csound.com/docs/manual/prints.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.csd` | [hello.csd](hello.csd) verified |
