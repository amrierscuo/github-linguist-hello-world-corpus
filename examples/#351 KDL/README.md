# #351 KDL

Voce canonica `KDL`, tipo `data`, language_id `931123626`.

Represent greeting as a value of a node in the KDL Document Language and verify its data and properties.

## Toolchain and reproduction

Existing KDL - JS document parser, kdljs 0.3.0. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

KDL - JS 0.3.0 on Node.js 22.20.0. The document uses a compatible form of the node language: greeting, string value and language=en property.

Comando/procedura from the directory of the example, unless explicit indications:

```text
npm install --prefix .tools kdljs@0.3.0; node verify.cjs .tools
```

Expected result: One greeting node, Hello, World! value, language=en; PASS.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The existing implementation analyses the document and must report zero errors. The flags concern the data model read by the parser; not an application that uses that model.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://kdl.dev/spec/](https://kdl.dev/spec/)
- [https://github.com/kdl-org/kdl-js](https://github.com/kdl-org/kdl-js)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.kdl` | [hello.kdl](hello.kdl) verified |
