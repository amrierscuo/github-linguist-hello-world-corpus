# #221 Futhark

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Fill Futhark and get the 13 byte UTF - 8 by Hello, World! from the main entry point.

Futhark is a pure language: the strings are array u8. main concatena two strings and the CLI generated program returns the numerical array. The verification compares all the bytes of output with greeting; the runtime does not offer a textual print in the source.

## Toolchain and reproduction

Futhark 0.27.1, GHC 9.10.3 build ufficiale; GNU C 13.3.0 in WSL

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
futhark check hello.fut
futhark c hello.fut -o hello
```

```text
./hello
```

## Expected result and status

[72u8, 101u8, 108u8, 108u8, 111u8, 44u8, 32u8, 87u8, 111u8, 114u8, 108u8, 100u8, 33u8]

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://futhark.readthedocs.io/en/latest/language-reference.html
- https://futhark.readthedocs.io/en/latest/usage.html
- https://github.com/diku-dk/futhark/releases/tag/v0.27.1

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.fut` | [hello.fut](hello.fut) verified |
