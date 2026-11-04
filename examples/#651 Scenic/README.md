# #651 Scenic

Fill out a Scenic scenario that exposes a parameter of greeting.

## Toolchain

Scenic scenario compiler

## Procedure

scenic hello.scenic; check the greeting parameter in the compiled scenario.

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.

The goal is the string parameter of the scenario; no physical simulation is invented.

Remaining requirements:
- Scenic compiler/simulator non predisposti.

## Primary sources

- [https://docs.scenic-lang.org/en/latest/syntax_guide.html](https://docs.scenic-lang.org/en/latest/syntax_guide.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.scenic` | [hello.scenic](hello.scenic) created; verification pending |
