# #232 GN

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Evaluate a GN build and produce greeting.txt to a true Ninja action.

.gn seleziona il buildconfig originale e l’interprete Python per le action. BUILD.gn definisce un toolchain minimale con stamp e una action. hello.py è una fixture che scrive l’output richiesto. La verifica passa tramite GN e Ninja, non esegue la fixture da sola.

## Toolchain and reproduction

GN 1000 (03d10f1), pacchetto Ubuntu generate-ninja; Ninja 1.11.1; Python 3.12.3

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
gn gen out
```

```text
ninja -C out greeting
```

## Expected result and status

Action reale produce out/gen/greeting.txt esattamente Hello, World! seguito da newline; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://gn.googlesource.com/gn/+/main/docs/quick_start.md
- https://gn.googlesource.com/gn/+/main/docs/reference.md
- https://ninja-build.org/manual.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.gn` | [.gn](.gn), [BUILD.gn](BUILD.gn), [BUILDCONFIG.gn](BUILDCONFIG.gn) verified |
| `.gni` | [hello.gni](variants/ext-gni-2e676e69/hello.gni) created; verification pending |
