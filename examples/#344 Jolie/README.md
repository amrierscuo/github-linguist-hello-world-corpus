# #344 Jolie

Voce canonica `Jolie`, tipo `programming`, language_id `998078858`.

Call the Console Jolie library to print the greeting from the main block.

## Toolchain and reproduction

Required genuine toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

It requires the Jolie and console.iol interpreter of the same distribution, with JVM compatible. The program invokes println@Console according to the library protocol.

Comando/procedura from the directory of the example, unless explicit indications:

```text
jolie hello.ol
```

Expected result: Jolie accepts and executes the program; Hello, World!.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

The interpreter and the library are not configured; it does not deduce validity from the similarity with other languages.

Remaining requirements:

- Jolie interpreter and console.iol standard library are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.jolie-lang.org/](https://www.jolie-lang.org/)
- [https://docs.jolie-lang.org/v1.12.x/language-tools-and-standard-library/basics/fault-handling/scopes-and-faults/README.html](https://docs.jolie-lang.org/v1.12.x/language-tools-and-standard-library/basics/fault-handling/scopes-and-faults/README.html)
- [https://github.com/jolie/jolie](https://github.com/jolie/jolie)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ol` | [hello.ol](hello.ol) created; verification pending |
| `.iol` | [hello.iol](variants/iol-77ad5fa4/hello.iol) created; verification pending |
