# #767 WebIDL

Voce canonica `WebIDL`, tipo `programming`, language_id `395`.

Original WebIDL Contract: enum GreetingText with `Hello, World!` value and namespace Greeting exposed to Window, with hello() method that returns that enum.

## Toolchain and reproduction

webidl2 / Node.js 22.20.0, 24.5.0. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Node.js 22.20.0 and webidl2, version in the log. `<prefisso-npm>/node_modules/webidl2` must be the original package.

Comando/procedura from the directory of the example, unless explicit indications:

```text
node verify.cjs <prefisso-npm>
```

Expected result: Hello, World! and PASS for enum and signing of the contract.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

webidl2 performs parsing and validation. The driver controls enum, value, namespace and type returned. The declared behavior is the IDL verified contract; no binding browser implementation is established.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://webidl.spec.whatwg.org/](https://webidl.spec.whatwg.org/)
- [https://github.com/w3c/webidl2.js](https://github.com/w3c/webidl2.js)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.webidl` | [hello.webidl](hello.webidl) verified |
