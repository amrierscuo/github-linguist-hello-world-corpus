# #263 Golo

Voce canonica `Golo`, tipo `programming`, language_id `133`.

Fill in and execute a Golo module with main, local binding and concatenation.

## Toolchain and reproduction

Official Eclipse Golo compiler and JVM runtime, 3.4.0. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Eclipse Golo 3.4.0 portable and JDK 21. The test recalls org.eclipse.golo.cli.Main with the classpath of JAR of the original distribution.

Comando/procedura from the directory of the example, unless explicit indications:

```text
golo check --files hello.golo; golo golo --files hello.golo
```

Expected result: Both exit 0 commands; print out the exact greeting.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Check and fill in the flight are executed by the original Eclipse compiler. The file ends with newline, significant for the syntax Golo.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://golo-lang.org/](https://golo-lang.org/)
- [https://golo-lang.github.io/documentation/next/](https://golo-lang.github.io/documentation/next/)
- [https://github.com/eclipse-archived/golo-lang](https://github.com/eclipse-archived/golo-lang)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.golo` | [hello.golo](hello.golo) verified |
