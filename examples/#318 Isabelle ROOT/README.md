# #318 Isabelle ROOT

Definire una sessione Isabelle ROOT che compila la teoria originale del saluto.

## Toolchain

Isabelle/HOL; versione da registrare

## Comandi e procedura

isabelle build -D . Hello

## Risultato atteso

Sessione Hello basata su HOL risolta; teoria Hello importata e lemma/value del saluto accettati.

## Stato

Sintassi e semantica in attesa.

ROOT è il file canonico della sessione. Hello.thy è incluso come consumer per rendere verificabile il risultato della build; non si dichiara verifica del formato tramite un parser fatto qui.

Requisiti residui:
- Isabelle session build non disponibile; ROOT e consumer restano pending.

## Fonti primarie

- [https://isabelle.in.tum.de/doc/system.pdf](https://isabelle.in.tum.de/doc/system.pdf)
