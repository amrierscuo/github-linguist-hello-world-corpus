# #318 Isabelle ROOT

Define a Isabelle ROOT session that compiles the original greeting theory.

## Toolchain

Isabelle/HOL; versione da registrare

## Commands and procedure

isabelle build -D . Hello

## Expected result

Hello session based on HOL resolved; imported Hello theory and lemma/value of greeting accepted.

## Status

Syntax and behavioral verification pending.

ROOT is the canonical file of the session. Hello.thy is included as a consumer to make the build result verifiable; it does not declare the format verification by a parser made here.

Remaining requirements:
- Isabelle session build unavailable; ROOT e consumer restano pending.

## Primary sources

- [https://isabelle.in.tum.de/doc/system.pdf](https://isabelle.in.tum.de/doc/system.pdf)
