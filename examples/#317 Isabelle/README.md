# #317 Isabelle

Define greeting in Isabelle/HOL, demonstrate its value and evaluate it.

## Toolchain

Isabelle/HOL; versione da registrare

## Commands and procedure

isabelle build -D. Hello; or open Hello.thy in Isabelle/jEdit and check value greeting

## Expected result

Teoria accettata, lemma greeting_correct dimostrato; value restituisce la stringa Hello, World!.

## Status

Syntax and behavioral verification pending.

The original example uses a HOL string, definition, test with simp and value command; the goal is a valutazione/prova, not console output of a generic program. ROOT provides context.

Remaining requirements:
- Isabelle and HOL image not available; type check/proof/value pending.

## Primary sources

- [https://isabelle.in.tum.de/doc/tutorial.pdf](https://isabelle.in.tum.de/doc/tutorial.pdf)
- [https://isabelle.in.tum.de/doc/isar-ref.pdf](https://isabelle.in.tum.de/doc/isar-ref.pdf)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.thy` | [Hello.thy](Hello.thy) created; verification pending |
