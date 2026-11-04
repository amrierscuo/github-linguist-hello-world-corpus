# #141 Csound

The canonical entry and order come from the corpus's `reference/languages.yml`. Sources and fixtures are original; any dumps or bundles come from the stated tools.

## Goal

Perform a Csound orchestra that prints Hello, World! at the initialization of instr 1.

hello.orc contains the orchestra program; schedule.sco activates the tool. Greeting comes from the built-in opacode prints. -n disabled audio output; no audio device or audio file is used.

## Toolchain and reproduction

Csound 6.18, pacchetto Ubuntu 6.18.1+dfsg-1ubuntu4 x86_64

Commands in the example folder with the toolchain available in PATH. Use a temporary copy: databases, objects, audio and other test outputs do not belong to the corpus.

```text
csound -n -d -m0 hello.orc schedule.sco
```

## Expected result and status

Messaggio Hello, World! seguito da newline; 0 errors in performance e exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records versions and provenance, SHA-256 of the source, actual commands, exit, stdout and stderr normalized.

## Primary sources

- https://csound.com/docs/manual/prints.html
- https://csound.com/docs/manual/CommandFlags.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.orc` | [hello.orc](hello.orc), [consumer.orc](variants/ext-udo-2e75646f/consumer.orc) created; verification pending |
| `.udo` | [hello.udo](variants/ext-udo-2e75646f/hello.udo) created; verification pending |
