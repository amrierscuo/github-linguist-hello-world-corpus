# #293 Haskell

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Interpret Haskell98 and print the value greeting = Hello, World!.

The Main module states greeting::String and main:: IO (). ++ concatena stringhe and putStrLn realizes the IO. The test uses the authentic Haskell Hugs interpreter in + 98 mode, with HUGSDIR and search path of isolated libraries.

## Toolchain and reproduction

Hugs98 September2006, pacchetto98.200609.21-6build3 e librerie bundled Ubuntu

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
runhugs +98 Hello.hs
```

## Expected result and status

stdout esattamente Hello, World! seguito da newline; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://www.haskell.org/hugs/
- https://www.haskell.org/onlinereport/haskell2010/haskellch9.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.hs` | [Hello.hs](Hello.hs), [Greeting.hs](variants/hs-boot-9862d855/Greeting.hs), [Audience.hs](variants/hs-boot-9862d855/Audience.hs), [Main.hs](variants/hs-boot-9862d855/Main.hs) created; verification pending |
| `.hs-boot` | [Greeting.hs-boot](variants/hs-boot-9862d855/Greeting.hs-boot) created; verification pending |
| `.hsc` | [hello.hsc](variants/hsc-700d6b1e/hello.hsc) created; verification pending |
