# #817 hoon

Evaluate a Hoon string in the gate of a say generator.

## Toolchain

Urbit Hoon compiler/dojo

## Procedure

Insert hello.hoon into the test pier as gen/hello.hoon and invoke +hello in the dojo.

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.

Original say generator structure: external gate produces %say and inner gate returns a %noun cord.

Remaining requirements:
- Urbit pier/compiler Hoon unavailable; type check of the generator and result pending.

## Primary sources

- [https://docs.urbit.org/hoon/](https://docs.urbit.org/hoon/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.hoon` | [hello.hoon](hello.hoon) created; verification pending |
