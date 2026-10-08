# #384 LilyPond

Impaginare una breve partitura LilyPond originale con titolo Hello, World!.

## Toolchain

LilyPond 2.24 compatibile; versione effettiva da registrare

## Comandi e procedura

lilypond --svg -o build/hello hello.ly

## Risultato atteso

SVG della partitura contiene il titolo Hello, World! e quattro note originali.

## Stato

Sintassi e semantica in attesa.

Le note c d e c e l’impaginazione sono originali. Il goal è la partitura con titolo, non riproduzione vocale del testo. Nessuno spartito esterno o font redistribuito.

Requisiti residui:
- Toolchain LilyPond/font/rendering non preparata; compilazione e lettura SVG pending.

## Fonti primarie

- [https://lilypond.org/doc/v2.24/Documentation/learning/](https://lilypond.org/doc/v2.24/Documentation/learning/)
- [https://lilypond.org/doc/v2.24/Documentation/usage/command_002dline-usage](https://lilypond.org/doc/v2.24/Documentation/usage/command_002dline-usage)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ly` | [hello.ly](hello.ly), [driver.ly](variants/ily-225ac663/driver.ly) creato, verifiche pendenti |
| `.ily` | [hello.ily](variants/ily-225ac663/hello.ily) creato, verifiche pendenti |
