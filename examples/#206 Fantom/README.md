# #206 Fantom

Voce canonica `Fantom`, tipo `programming`, language_id `110`.

Fill out the script Fantom Hello and concatenate greeting in the main method.

## Toolchain and reproduction

Official Fantom JVM distribution, 1.0.83. Test environment: **Windows x64**.

Portable distribution Fantom 1.0.83 with JVM. The test directly uses java -Dfan.home =<fantom> -cp <fantom>/ lib/java/sys.jar fanx.tools.Fan hello.fan. The log retains the actual command and the JARhash.

Comando/procedura from the directory of the example, unless explicit indications:

```text
fan hello.fan
```

Exit 0; stdout exactly Hello, World! followed by newline.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The -version Fantom command returns 3 code in the distribution used, while reporting the full version; the output ends 0 and produces the exact greeting.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sources verified in staging. The only available probe do not attest parsing
or execution. Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://fantom.org/](https://fantom.org/)
- [https://github.com/fantom-lang/fantom/releases/tag/v1.0.83](https://github.com/fantom-lang/fantom/releases/tag/v1.0.83)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.fan` | [hello.fan](hello.fan) verified |
