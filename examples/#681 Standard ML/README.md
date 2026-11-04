# #681 Standard ML

Voce canonica `Standard ML`, tipo `programming`, language_id `357`.

Fill and execute a standard ML source with concatenation and print.

## Toolchain and reproduction

Original Poly/ML Standard ML compiler/interpreter, Poly/ML 5.7.1 Release. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Poly/ML 5.7.1 autentico Ubuntu, estratto sotto work.

Comando/procedura from the directory of the example, unless explicit indications:

```text
poly --script hello.sml
```

Expected result: Hello, World! in the conformed result, according to the framework described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Compiler/interpreter originali, stdout esatto e termine normale.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.polyml.org/documentation/](https://www.polyml.org/documentation/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ml` | [hello.ml](variants/ml-88c80c27/hello.ml) created; verification pending |
| `.fun` | [hello.fun](variants/fun-28c9c936/hello.fun) created; verification pending |
| `.sig` | [hello.sig](variants/sig-21be57d9/hello.sig) created; verification pending |
| `.sml` | [hello.sml](hello.sml), [main.sml](variants/sig-21be57d9/main.sml) created; verification pending |
