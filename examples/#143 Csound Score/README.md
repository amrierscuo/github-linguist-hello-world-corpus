# #143 Csound Score

The canonical entry and order come from the corpus's `reference/languages.yml`. Sources and fixtures are original; any dumps or bundles come from the stated tools.

## Goal

Read a p4 string from a Csound score and print it through the support orchestra.

hello.sco is an authentic score: i-statement with tool, time, duration and string parameter. reader.orc is a fixture that reads p4 through strget. Greeting belongs to the score, is not replaced by a constant print in the fixture. The optional warning directory is registered.

## Toolchain and reproduction

Csound 6.18, pacchetto Ubuntu 6.18.1+dfsg-1ubuntu4 x86_64

Commands in the example folder with the toolchain available in PATH. Use a temporary copy: databases, objects, audio and other test outputs do not belong to the corpus.

```text
csound -n -d -m0 reader.orc hello.sco
```

## Expected result and status

The p4 parameter of the first event is Hello, World! and the runtime prints that value; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records versions and provenance, SHA-256 of the source, actual commands, exit, stdout and stderr normalized.

## Primary sources

- https://csound.com/docs/manual/ScoreIStatement.html
- https://csound.com/docs/manual/strget.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.sco` | [hello.sco](hello.sco) verified |
