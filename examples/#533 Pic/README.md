# #533 Pic

Voce canonica `Pic`, tipo `markup`, language_id `425`.

Draw a box labeled by the preprocessor Pic and make it in text.

## Toolchain and reproduction

Genuine GNU Pic and groff ASCII renderr, GNU pic (groff) version 1.23.0. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

GNU Pic/groff 1.23.0 autentici.

Comando/procedura from the directory of the example, unless explicit indications:

```text
pic hello.pic; groff -p -Tascii hello.pic
```

Expected result: The conformed result contains Hello, World!, according to the framework described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Pic generates primitive troffs; groff makes a box with Hello, World! text. A warning of grotty on the thickness of the line does not prevent rendering.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.gnu.org/software/groff/manual/groff.html#Pictures](https://www.gnu.org/software/groff/manual/groff.html#Pictures)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pic` | [hello.pic](hello.pic) verified |
| `.chem` | [hello.chem](variants/chem-e7e80156/hello.chem) created; verification pending |
