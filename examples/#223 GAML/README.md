# #223 GAML

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Start a GAMA model and write Hello, World! in the console.

The model declares global/init and a minimal GUI experiment. write uses GAML concatenation; it is not a Java program or a generic configuration file.

## Toolchain and reproduction

GAMA Platform con runtime GAML; versione effettiva da registrare

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
Aprire hello.gaml in GAMA, avviare l’esperimento greeting.
```

## Expected result and status

The global/init section writes Hello, World! once.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no native parser/compilatore/runtime performed for this item.

Commitments: GAMA/Eclipse and runtime GAML unprepared; no parser or GAMA experiment was executed.

## Primary sources

- https://gama-platform.org/wiki/Introduction
- https://gama-platform.org/wiki/next/ModelOrganization

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.gaml` | [hello.gaml](hello.gaml) created; verification pending |
