# #145 Cue Sheet

The canonical entry and order come from the corpus's `reference/languages.yml`. Sources and fixtures are original; any dumps or bundles come from the stated tools.

## Goal

Analyze a Cue Sheet and recover the Hello, World! title of audio track 01.

hello.cue uses FILE, TRACK, TITLE and INDEX in CDRWIN/CUE sheet format. It is not a program in CUE language. The original fixture generates a second silence PCM only in the temporary copy; cueprint verification parser and metadata, without mastering

## Toolchain and reproduction

cuetools package 1.4.1-0.2; cueprint declares 1.4.0; Python 3.13.9 for fixtures

Commands in the example folder with the toolchain available in PATH. Use a temporary copy: databases, objects, audio and other test outputs do not belong to the corpus.

```text
python make_fixture.py
cueprint -i cue -n 1 -t %t hello.cue
```

## Expected result and status

Title extracted exactly Hello, World!, without newline added by the %t template; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records versions and provenance, SHA-256 of the source, actual commands, exit, stdout and stderr normalized.

## Primary sources

- https://www.gnu.org/software/ccd2cue/manual/html_node/CUE-sheet-format.html
- https://manpages.debian.org/bullseye/cuetools/cueprint.1.en.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cue` | [hello.cue](hello.cue) verified |
