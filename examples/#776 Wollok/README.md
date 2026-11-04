# #776 Wollok

Voce canonica `Wollok`, tipo `programming`, language_id `632745969`.

Subject Wollok original greeting with hello( method), imported from a program that sends the result to console.println.

## Toolchain and reproduction

wollok-ts / Node.js 22.20.0, 4.3.0. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Node.js 22.20.0 and wollok-ts 4.3.0 of the Uqbar project. Install the package in an external prefix and set NODE_PATH on its node_modules.

Comando/procedura from the directory of the example, unless explicit indications:

```text
node verify.cjs
```

Expected result: Hello, World! produced by the program and PASS.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The original parser analyzes both sources, buildEnvironment connects them with WRE and the original interpreter performs the program.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://uqbar-project.github.io/wollok-ts/](https://uqbar-project.github.io/wollok-ts/)
- [https://github.com/uqbar-project/wollok-ts](https://github.com/uqbar-project/wollok-ts)
- [https://www.wollok.org/](https://www.wollok.org/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.wlk` | [greeting.wlk](greeting.wlk) verified |
