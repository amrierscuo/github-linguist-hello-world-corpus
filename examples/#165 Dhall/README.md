# #165 Dhall

Evaluate an interpolated Text Dhall value and get Hello, World! without newline.

## Toolchain

Dhall 1.42.2

## Commands and procedure

dhall version; dhall type --file hello.dhall; dhall text --file hello.dhall

## Expected result

Tipo Text; export text restituisce esattamente Hello, World!, exit 0.

## Status

syntax and behavior verified.

The type checker and the official normalizer solve targets: Text and interpolation. Source does not matter network resources.

Actual verification of 2026-10-08T11:56:10.980886+00:00 on Windows x64: [log](verification/result.json).
Hash of sorgenti/checker, real versions and commands, output codes, stdout/stderr and test limits are in the log.

## Primary sources and format reference

- [https://docs.dhall-lang.org/tutorials/Getting-started_Generate-JSON-or-YAML.html](https://docs.dhall-lang.org/tutorials/Getting-started_Generate-JSON-or-YAML.html)
- [https://github.com/dhall-lang/dhall-haskell/releases/tag/1.42.2](https://github.com/dhall-lang/dhall-haskell/releases/tag/1.42.2)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.dhall` | [hello.dhall](hello.dhall) verified |
