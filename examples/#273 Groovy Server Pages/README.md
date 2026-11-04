# #273 Groovy Server Pages

Voce canonica `Groovy Server Pages`, tipo `programming`, language_id `143`.

Render a GSP text/plain page by interpolating the name model variable.

## Toolchain and reproduction

Required genuine toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Place hello.gsp in grails-app/views and provide the model from the controller.

Comando/procedura from the directory of the example, unless explicit indications:

```text
Applicazione Grails locale: render(view: "/hello", model: [name: "World"]); richiedere la route locale e confrontare il body
```

Expected result: Answer text/plain Hello, World!.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

The ${name} page and expression are GSP real. A generic Groovy renderr would not demonstrate the management of the directive or the Grails engine; no one is used as proof.

Remaining requirements:

- Native Grails GSP engine and web application context are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://grails.apache.org/docs-legacy-gsp/6.0.0-M1/guide/](https://grails.apache.org/docs-legacy-gsp/6.0.0-M1/guide/)
- [https://grails.apache.org/guides/creating-your-first-grails-app/4/guide/index.html](https://grails.apache.org/guides/creating-your-first-grails-app/4/guide/index.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.gsp` | [hello.gsp](hello.gsp) created; verification pending |
