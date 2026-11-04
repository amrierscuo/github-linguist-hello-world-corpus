# #213 Fluent

Voce canonica `Fluent`, tipo `programming`, language_id `206353404`.

Analyze the Fluent localization message and render Hello, World! with a variable name; check also Reader.

## Toolchain and reproduction

Official Mozilla Fluent syntax AST and runtime bundle, @fluent/syntax 0.19.0; @fluent/bundle 0.19.1; v22.20.0. Test environment: **Windows x64**.

Node.js 22.20.0 and official Mozilla Fluent packages set to the specified versions. .tools is placed in a work copy.

Comando/procedura from the directory of the example, unless explicit indications:

```text
npm install --prefix .tools @fluent/syntax@0.19.0 @fluent/bundle@0.19.1; node verify.cjs .tools hello.ftl
```

Expected result: World greeting and correct Reader control; PASS.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Il parser ufficiale deve produrre zero Junk; FluentBundle riceve una FluentResource e controlla errori e rendering parametrico. useIsolating=false rende il confronto testuale esplicito. Questa .ftl è localizzazione Fluent.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sources verified in staging. The only available probe do not attest parsing
or execution. Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://projectfluent.org/](https://projectfluent.org/)
- [https://github.com/projectfluent/fluent.js](https://github.com/projectfluent/fluent.js)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ftl` | [hello.ftl](hello.ftl) verified |
