# #384 LilyPond

Engage a short original LilyPond score with Hello, World! title.

## Toolchain

LilyPond 2.24 compatibile; versione effettiva da registrare

## Commands and procedure

lilypond --svg -o build/hello hello.ly

## Expected result

SVG of the score contains the title Hello, World! and four original notes.

## Status

Syntax and behavioral verification pending.

The goal is the score with title, not vocal reproduction of the text. No external score or redistributed font.

Remaining requirements:
- Toolchain LilyPond/font/rendering non preparata; compilazione e lettura SVG pending.

## Primary sources

- [https://lilypond.org/doc/v2.24/Documentation/learning/](https://lilypond.org/doc/v2.24/Documentation/learning/)
- [https://lilypond.org/doc/v2.24/Documentation/usage/command_002dline-usage](https://lilypond.org/doc/v2.24/Documentation/usage/command_002dline-usage)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ly` | [hello.ly](hello.ly), [driver.ly](variants/ily-225ac663/driver.ly) created; verification pending |
| `.ily` | [hello.ily](variants/ily-225ac663/hello.ily) created; verification pending |
