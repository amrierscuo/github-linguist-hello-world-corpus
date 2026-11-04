# #266 Gradle

Voce canonica `Gradle`, tipo `data`, language_id `136`.

Record a Gradle task in the Groovy DSL and print its greeting during doLast.

## Toolchain and reproduction

Official Gradle distribution Groovy DSL, 8.14.3; JDK 21. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Distribuzione Gradle ufficiale 8.14.3 con JDK 21. Il progetto non usa plugin esterni o repository. Eseguire in copia con GRADLE_USER_HOME isolata.

Comando/procedura from the directory of the example, unless explicit indications:

```text
gradle --no-daemon --offline --console=plain --max-workers=1 -q hello
```

Exit 0; Hello, World! followed by newline.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Il launcher ufficiale configura settings.gradle e build.gradle, registra hello e ne esegue l’azione. La prova termina 0 con stdout esatto.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://docs.gradle.org/8.14.3/userguide/tutorial_using_tasks.html](https://docs.gradle.org/8.14.3/userguide/tutorial_using_tasks.html)
- [https://docs.gradle.org/8.14.3/userguide/writing_build_scripts.html](https://docs.gradle.org/8.14.3/userguide/writing_build_scripts.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.gradle` | [build.gradle](build.gradle), [settings.gradle](settings.gradle) verified |
