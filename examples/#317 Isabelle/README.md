# #317 Isabelle

Definire greeting in Isabelle/HOL, dimostrarne il valore e valutarlo.

## Toolchain

Isabelle/HOL; versione da registrare

## Comandi e procedura

isabelle build -D . Hello; oppure aprire Hello.thy in Isabelle/jEdit e verificare value greeting

## Risultato atteso

Teoria accettata, lemma greeting_correct dimostrato; value restituisce la stringa Hello, World!.

## Stato

Sintassi e semantica in attesa.

L’esempio originale usa una stringa HOL, definizione, prova con simp e comando value; il goal è una valutazione/prova, non output console di un programma generico. ROOT fornisce il contesto.

Requisiti residui:
- Isabelle e immagine HOL non disponibili; type check/proof/value pending.

## Fonti primarie

- [https://isabelle.in.tum.de/doc/tutorial.pdf](https://isabelle.in.tum.de/doc/tutorial.pdf)
- [https://isabelle.in.tum.de/doc/isar-ref.pdf](https://isabelle.in.tum.de/doc/isar-ref.pdf)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.thy` | [Hello.thy](Hello.thy) creato, verifiche pendenti |
