# #448 Motoko

Voce canonica `Motoko`, tipo `programming`, language_id `202937027`.

Run a Motoko query of a local actor and check a second string parameter.

## Toolchain and reproduction

Authentic Motoko compiler and actor interpreter via official-linked Node bindings — node-motoko 5.0.0. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Complete Motoko through the binding Node quoted by the official project; the version actually used is in the log.

Comando/procedura from the directory of the example, unless explicit indications:

```text
npm install --prefix .tools motoko; node verify.cjs .tools
```

Expected result: The Motoko result contains "Hello, World!": Text; PASS.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

mo.check verifies the type, mo.run executes the actor and query, and the Axis Reader controls the parameter. Scope: local interpreter, without canister deployment.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://docs.internetcomputer.org/languages/motoko/reference/compiler-ref/](https://docs.internetcomputer.org/languages/motoko/reference/compiler-ref/)
- [https://github.com/caffeinelabs/motoko](https://github.com/caffeinelabs/motoko)
- [https://github.com/caffeinelabs/node-motoko](https://github.com/caffeinelabs/node-motoko)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mo` | [hello.mo](hello.mo) verified |
