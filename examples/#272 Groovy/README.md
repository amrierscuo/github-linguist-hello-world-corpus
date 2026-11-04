# #272 Groovy

Voce canonica `Groovy`, tipo `programming`, language_id `142`.

Interpolate a variable in a GString Groovy and print it.

## Toolchain and reproduction

Official Apache Groovy compiler/runtime jar — Groovy Version: 3.0.24 JVM: 21.0.12.1 Vendor: Microsoft OS: Windows 11. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Apache Groovy 3.0.24 official, JAR original present in the distribution Gradle 8.14.3; JDK 21. The test invokes java -cp groovy-3.0.24.jar groovy.ui.GroovyMain hello.groovy.

Comando/procedura from the directory of the example, unless explicit indications:

```text
groovy hello.groovy
```

Exit 0; exact greeting followed by newline.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Il compiler/runtime Groovy autentico analizza ed esegue il sorgente. Non è necessario un progetto Gradle per questa voce.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://groovy-lang.org/syntax.html#_string_interpolation](https://groovy-lang.org/syntax.html#_string_interpolation)
- [https://groovy-lang.org/](https://groovy-lang.org/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.groovy` | [hello.groovy](hello.groovy), [render.groovy](variants/ext-grt-2e677274/render.groovy), [render.groovy](variants/ext-gtpl-2e6774706c/render.groovy) syntax and behavior verified |
| `.grt` | [hello.grt](variants/ext-grt-2e677274/hello.grt) syntax and behavior verified |
| `.gtpl` | [hello.gtpl](variants/ext-gtpl-2e6774706c/hello.gtpl) syntax and behavior verified |
| `.gvy` | [hello.gvy](variants/ext-gvy-2e677679/hello.gvy) syntax and behavior verified |

## Additional extension verification

- `.groovy`: verified on November 4, 2026. [Evidence](verification/native_20261104_272_variants_result.json).
- `.grt`: verified on November 4, 2026. [Evidence](verification/native_20261104_272_variants_result.json).
- `.gtpl`: verified on November 4, 2026. [Evidence](verification/native_20261104_272_variants_result.json).
- `.gvy`: verified on November 4, 2026. [Evidence](verification/native_20261104_272_variants_result.json).
