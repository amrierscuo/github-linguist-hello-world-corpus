# #362 KoLmafia ASH

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Interpretare KoLmafia ASH e stampare Hello, World!.

The main input point chains a string variable with print. The test requires the parser/interprete ASH of the KoLmafia distribution.

## Toolchain and reproduction

KoLmafia/ASH originale; versione da registrare

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
Nel CLI KoLmafia: call hello.ash
```

## Expected result and status

Console contains Hello, World!.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no native parser/compilatore/runtime performed for this item.

Commitments: KoLmafia not prepared; no connection to the game performed.

## Primary sources

- https://github.com/kolmafia/kolmafia
- https://raw.githubusercontent.com/kolmafia/kolmafia/main/src/net/sourceforge/kolmafia/textui/Parser.java

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ash` | [hello.ash](hello.ash) created; verification pending |
