# #694 Swift

Voce canonica `Swift`, tipo `programming`, language_id `362`.

Run a Swift source with interpolation string and print.

## Toolchain and reproduction

Required genuine swift compiler/runtime, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Requires original Swift toolchain compatible with the system.

Comando/procedura from the directory of the example, unless explicit indications:

```text
swift hello.swift
```

Expected result: Hello, World! in the conformed result, according to the framework described.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Sorgente originale; compiler/runtime unavailable.

Remaining requirements:

- Required swift toolchain and matching execution/format resources are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://docs.swift.org/swift-book/documentation/the-swift-programming-language/guidedtour/](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/guidedtour/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.swift` | [hello.swift](hello.swift) created; verification pending |
