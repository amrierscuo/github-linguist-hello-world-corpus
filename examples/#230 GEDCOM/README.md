# #230 GEDCOM

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Analyze a GEDCOM 5.5.1 and recover a NOTE with Hello, World! value.

HEAD dichiara versione, formato e UTF-8; la NOTE top-level ha un identificatore e TRLR conclude il documento. La verifica usa Parser.parse_file(strict=True) della libreria originale e controlla la NOTE ottenuta. Non è una validazione completa di tutte le regole genealogiche dello standard.

## Toolchain and reproduction

python-gedcom 1.1.0, CPython 3.13.9

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
python verify.py
```

## Expected result and status

PASS: GEDCOM NOTE = Hello, World!; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://gedcom.io/specifications/ged551.pdf
- https://github.com/nickreynke/python-gedcom

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ged` | [hello.ged](hello.ged) verified |
