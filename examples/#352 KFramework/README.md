# #352 KFramework

Voce canonica `KFramework`, tipo `programming`, language_id `9479532`.

Define a small behavior K that rewrites the hello term in the greeting string value in the k cell.

## Toolchain and reproduction

Required genuine toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Requires K Framework with configured backend and builtin STRING modules.

Comando/procedura from the directory of the example, unless explicit indications:

```text
kompile hello.k --main-module HELLO --syntax-module HELLO; krun input.hello
```

Expected result: Filled definition; final k cell contains "Hello, World!".

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

The rule is a real behavior K rewrite; missing toolchain kompile/krun. No rules are interpreted with a homemade simulator.

Remaining requirements:

- K Framework kompile/krun and backend are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://kframework.org/docs/user_manual/](https://kframework.org/docs/user_manual/)
- [https://github.com/runtimeverification/k](https://github.com/runtimeverification/k)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.k` | [hello.k](hello.k) created; verification pending |
