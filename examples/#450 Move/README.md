# #450 Move

Voce canonica `Move`, tipo `programming`, language_id `638334599`.

Build a module in the original Move language and test the function that returns a string.

## Toolchain and reproduction

Required genuine toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Requires compiler/test runner move-language/move and the MoveStdlib indicated in Move.toml, with compatible version.

Comando/procedura from the directory of the example, unless explicit indications:

```text
move build; move test
```

Expected result: Hello, World!

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Module and original tests; toolchain Move unavailable. No account or blockchain deployment is required.

Remaining requirements:

- Original Move compiler/test runner and matching stdlib are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://github.com/move-language/move](https://github.com/move-language/move)
- [https://move-language.github.io/move/strings.html](https://move-language.github.io/move/strings.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.move` | [greeting.move](sources/greeting.move) created; verification pending |
