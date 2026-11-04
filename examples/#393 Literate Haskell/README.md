# #393 Literate Haskell

Play a Haskell-style Bird program that prints greetings.

## Toolchain

Genuine Hugs98 September 2006; Ubuntu package 98.200609.21-6build3 Haskell98 mode

## Commands and procedure

HUGSDIR=<libreria-hugs> runhugs +98 -P<percorsi-librerie-bundled> hello.lhs

## Expected result

Recognized alloys; main: IO (); Hello, World! output more newline.

## Status

syntax and behavior verified.

The original Hugs98 interpreter directly analyzes .lhs and controls the types; it has not been converted to .hs by a personal parser. Haskell98 libraries and base are those of the tool. It is a verification on the Haskell98 standard, without modern GHC claim.

Actual verification of 2026-10-08T12:51:44.086941+00:00 on WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://www.haskell.org/onlinereport/literate.html](https://www.haskell.org/onlinereport/literate.html)
- [https://www.haskell.org/hugs/](https://www.haskell.org/hugs/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.lhs` | [hello.lhs](hello.lhs) verified |
