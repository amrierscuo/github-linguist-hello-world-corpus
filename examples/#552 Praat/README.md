# #552 Praat

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Run a Praat script and write Hello, World! in the Info/stdout batch window.

audience$ è una stringa Praat. writeInfoLine usa il comando nativo; il runtime batch restituisce output UTF16LE, decodificato nel log e confrontato con il saluto. Nessun audio viene registrato o riprodotto.

## Toolchain and reproduction

Praat7.0.02 ufficiale Windows x64v1

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
Praat.exe --run hello.praat
```

## Expected result and status

Hello, World! seguito da newline; exit0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://www.fon.hum.uva.nl/praat/manual/Scripting.html
- https://github.com/praat/praat/releases/tag/v7.0.02

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.praat` | [hello.praat](hello.praat) verified |
