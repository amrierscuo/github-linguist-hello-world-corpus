# #267 Gradle Kotlin DSL

Voce canonica `Gradle Kotlin DSL`, tipo `data`, language_id `432600901`.

Record and run a Gradle task in the Kotlin DSL using an interpolated valley.

## Toolchain and reproduction

Official Gradle distribution Kotlin DSL, 8.14.3; JDK 21. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Official grade 8.14.3, Kotlin embedded 2.0.21 and JDK 21. Do not need Kotlin plugins downloaded. Run in a copy of work with Gradle cache isolated.

Comando/procedura from the directory of the example, unless explicit indications:

```text
gradle --no-daemon --offline --console=plain --max-workers=1 -q hello
```

Expected result: Task hello exit 0; exact greeting.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

build.gradle.kts and settings.gradle.kts are actually compiled by Kotlin DSL Gradle; they are not executed as a normal Kotlin application.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://docs.gradle.org/8.14.3/userguide/kotlin_dsl.html](https://docs.gradle.org/8.14.3/userguide/kotlin_dsl.html)
- [https://docs.gradle.org/8.14.3/userguide/tutorial_using_tasks.html](https://docs.gradle.org/8.14.3/userguide/tutorial_using_tasks.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.gradle.kts` | [build.gradle.kts](build.gradle.kts), [settings.gradle.kts](settings.gradle.kts) verified |
