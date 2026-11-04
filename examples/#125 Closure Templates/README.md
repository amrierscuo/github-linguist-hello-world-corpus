# #125 Closure Templates

Voce canonica: `Closure Templates`, tipo `markup`, `language_id: 357046146`.

Fill out the parametric Soy template and make Hello, World! in text mode; also check Hello, Reader! by changing the parameter.

## Toolchain and reproduction

Official Google Closure Templates SoyFileSet compiler and SoyTofu maker, 2024-02-26. Test environment: **Windows x64**.

Scaricare il JAR ufficiale Maven com.google.template:soy:2024-02-26 con classifier SoyToJsSrcCompiler in .tools. Contiene anche SoyFileSet/SoyTofu e le dipendenze Java. Richiede un JDK; qui è stato usato OpenJDK 21.0.12.1.

Comando/procedura from the example directory, except the build directory explicitly indicated:

```text
java --class-path .tools/soy-2024-02-26-SoyToJsSrcCompiler.jar SoyCheck.java hello.soy
```

Exit 0; Hello, World! and PASS: official Soy compile/render and parameter control.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

SoyCheck.java delegation parsing, typecheck and rendering to official Soy API. Two depreciation alerts for API legacy SoyFileSet.builder /compileTofu do not prevent positive verification.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain versions and SHA-256 values for the artifacts. The `path_normalization` property documents
local route replacements. `<corpus>` identifies the relative files included in
final corpus, which were first verified in the staging directory.
sources remain those identified by checksums. The only offspring of availability
instruments do not attest parsing or execution.
in the work directory and are not included in the corpus.

## Primary sources

- [https://github.com/google/closure-templates](https://github.com/google/closure-templates)
- [https://github.com/google/closure-templates/blob/master/documentation/reference/templates.md](https://github.com/google/closure-templates/blob/master/documentation/reference/templates.md)
- [https://repo.maven.apache.org/maven2/com/google/template/soy/2024-02-26/](https://repo.maven.apache.org/maven2/com/google/template/soy/2024-02-26/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.soy` | [hello.soy](hello.soy) verified |
