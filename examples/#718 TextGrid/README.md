# #718 TextGrid

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Analyze TextGrid and read the greeting from the label of the first interval.

Original TextGrid with an IntervalTier from0 to1 second. Praat reads the format and the driver questions the label: it does not need an audio file.

## Toolchain and reproduction

Praat7.0.02 originale

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
praat --run verify.praat
```

## Expected result and status

Label = Hello, World!, printed by the runtime.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://www.fon.hum.uva.nl/praat/manual/TextGrid_file_formats.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.TextGrid` | [hello.TextGrid](hello.TextGrid) verified |
