# #555 Processing

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Perform an original sketch Processing and print Hello, World!.

The Hello directory contains Hello.pde. setup declares a String variable, calls println and concludes the sketch with exit; preprocessing Processing is distinguished by javac on a generic C/Java file.

## Toolchain and reproduction

Processing Java mode originale; versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
processing-java --sketch=Hello --run
```

## Expected result and status

Hello, World! seguito da newline; exit0.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Impedimenti: Processing/Java-mode preprocessor e host non preparati.

## Primary sources

- https://processing.org/reference/println_.html
- https://processing.org/reference/exit_.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pde` | [Hello.pde](Hello/Hello.pde) created; verification pending |
