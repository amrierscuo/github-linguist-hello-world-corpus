# #253 Glyph

Caricare PWI_Glyph 2 in Pointwise e scrivere Hello, World! nella finestra messaggi.

## Toolchain

Cadence Fidelity Pointwise con PWI_Glyph 2; versione/licenza runtime da registrare

## Comandi e procedura

Aprire hello.glf tramite Script > Execute in Pointwise; oppure usare il tclsh fornito da Pointwise per hello.glf

## Risultato atteso

Package PWI_Glyph caricato; puts scrive il saluto più newline.

## Stato

Sintassi e semantica in attesa.

Identificazione originale: Glyph è l’interfaccia Tcl del mesher Pointwise, come documentato dal vendor. package require PWI_Glyph 2 impedisce di confondere un tclsh generico con il runtime Glyph. Non viene contattato un server o consumata una licenza.

Requisiti residui:
- Cadence Pointwise/PWI_Glyph 2 runtime non disponibile; package load e puts non eseguiti.

## Fonti primarie

- [https://pointwise.github.io/](https://pointwise.github.io/)
- [https://www.cadence.com/doc/user-manual/getting-started/command-line-options.html](https://www.cadence.com/doc/user-manual/getting-started/command-line-options.html)
- [https://github.com/pointwise/GlyphClientPython](https://github.com/pointwise/GlyphClientPython)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.glf` | [hello.glf](hello.glf) creato, verifiche pendenti |
