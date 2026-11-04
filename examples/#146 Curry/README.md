# #146 Curry

The canonical entry and order come from the corpus's `reference/languages.yml`. Sources and fixtures are original; any dumps or bundles come from the stated tools.

## Goal

Perform the IO main action of Curry and print Hello, World!.

Hello.curry declares a module and the main action:: IO (). ++ concatenate strings, putStrLn performs IO. Verification requires an authentic Curry compiler, with Prolog/Haskell runtimes provided for its implementation.

## Toolchain and reproduction

PAKCS o altra implementazione Curry; versione effettiva da registrare

Commands in the example folder with the toolchain available in PATH. Use a temporary copy: databases, objects, audio and other test outputs do not belong to the corpus.

```text
Nella REPL PAKCS: :load Hello
Poi valutare: main
Infine: :quit
```

## Expected result and status

stdout Hello, World! seguito da newline.

Artifact created: yes. syntax verified: no. behavior verified: no.

The source is documented; native parser/compilatore/runtime has not been performed for this item.

Commitments: PAKCS/KiCS2 and its runtime not available; no Curry parser has been executed.

## Primary sources

- https://www.curry-language.org/docs/tutorial/html/curry-tutorial.Ch3.S15.html
- https://www.curry-lang.org/pakcs/

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.curry` | [Hello.curry](Hello.curry) created; verification pending |
