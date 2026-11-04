# #364 Kotlin

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Fill in Kotlin/JVM and print Hello, World!.

The main function uses a string valley and interpolation. The test invokes the official JVM compiler and JVM, with jar generated only in work.

## Toolchain and reproduction

Kotlin2.4.21, OpenJDK21 Microsoft

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
kotlinc Hello.kt -include-runtime -d hello.jar
```

```text
java -jar hello.jar
```

## Expected result and status

stdout esattamente Hello, World! seguito da newline; exit0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://kotlinlang.org/docs/command-line.html
- https://github.com/JetBrains/kotlin/releases/tag/v2.4.21

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.kt` | [Hello.kt](Hello.kt) verified |
| `.ktm` | [hello.ktm](variants/ktm-5ead4c6e/hello.ktm) created; verification pending |
| `.kts` | [hello.kts](variants/kts-f3ce7309/hello.kts) created; verification pending |
