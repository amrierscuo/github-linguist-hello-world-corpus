# #523 Pact

Voce canonica `Pact`, tipo `programming`, language_id `756774415`.

Evaluate a binding and format of the Pact Kadena language in the local REPL.

## Toolchain and reproduction

Required genuine compiler/runtime, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

It requires the Pact interpreter of kadena-io/pact, with the REPL print function.

Comando/procedura from the directory of the example, unless explicit indications:

```text
pact; (load "hello.pact")
```

Expected result: The conformed result contains Hello, World!, according to the framework described.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Original Pact Source; toolchain absent. This entry indicates the Kadena smart contract language. No deployments or accounts needed.

Remaining requirements:

- Required pact compiler/interpreter and matching host libraries are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://pact-language.readthedocs.io/en/latest/pact-functions.html](https://pact-language.readthedocs.io/en/latest/pact-functions.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pact` | [hello.pact](hello.pact) created; verification pending |
