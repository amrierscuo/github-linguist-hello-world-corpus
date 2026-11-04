# #524 Pan

Voce canonica `Pan`, tipo `programming`, language_id `276`.

Fill out an object template Pan and get a JSON configuration with message.

## Toolchain and reproduction

Official Quattor Pan compiler, pan compiler version: 10.8. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Quattor Pan 10.8 official. The fat JAR has Main-Class Compiler which only prints the version; the true CLI is pan_compiler, used in the test.

Comando/procedura from the directory of the example, unless explicit indications:

```text
java -cp /path/to/panc-10.8.jar org.quattor.pan.pan_compiler --formats json --output-dir build greeting.pan
```

Expected result: The conformed result contains Hello, World!, according to the framework described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The authentic compiler generates greeting.json with exact message Hello, World!.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://quattor-pan.readthedocs.io/en/latest/pan-book/pan-book.html](https://quattor-pan.readthedocs.io/en/latest/pan-book/pan-book.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pan` | [greeting.pan](greeting.pan) verified |
