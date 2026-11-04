# #219 FreeMarker

Voce canonica `FreeMarker`, tipo `programming`, language_id `115`.

Upload an Apache FreeMarker template, interpolate name and verify rendering for World and Reader.

## Toolchain and reproduction

Official Apache FreeMarker template parser and engine, 2.3.34. Test environment: **Windows x64**.

Apache FreeMarker 2.3.34 official from Maven Central and JDK 21. Place the JAR in .tools out of deliverable; the Java helper uses the official API Configuration and Templates.

Comando/procedura from the directory of the example, unless explicit indications:

```text
java --class-path .tools/freemarker-2.3.34.jar FreeMarkerCheck.java .
```

Expected result: Hello, World! and PASS of parametric control.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

This .ftl is a FreeMarker template. The comparison controls the exact and newline content for two values, after the true parsing of the engine.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sources verified in staging. The only available probe do not attest parsing
or execution. Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://freemarker.apache.org/docs/dgui_quickstart_basics.html](https://freemarker.apache.org/docs/dgui_quickstart_basics.html)
- [https://freemarker.apache.org/docs/pgui_quickstart_all.html](https://freemarker.apache.org/docs/pgui_quickstart_all.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ftl` | [hello.ftl](hello.ftl) verified |
| `.ftlh` | [hello.ftlh](variants/ext-ftlh-2e66746c68/hello.ftlh) created; verification pending |
