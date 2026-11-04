# #253 Glyph

Upload PWI_Glyph 2 in Pointwise and write Hello, World! in the Messages window.

## Toolchain

Cadence Fidelity Pointwise con PWI_Glyph 2; versione/licenza runtime da registrare

## Commands and procedure

Open hello.glf via Script > Execute in Pointwise; or use the tclsh provided by Pointwise for hello.glf

## Expected result

Package PWI_Glyph loaded; puts writes the newest greeting.

## Status

Syntax and behavioral verification pending.

Identificazione originale: Glyph è l’interfaccia Tcl del mesher Pointwise, come documentato dal vendor. package require PWI_Glyph 2 impedisce di confondere un tclsh generico con il runtime Glyph. Non viene contattato un server o consumata una licenza.

Remaining requirements:
- Cadence Pointwise/PWI_Glyph 2 runtime non disponibile; package load e puts non eseguiti.

## Primary sources

- [https://pointwise.github.io/](https://pointwise.github.io/)
- [https://www.cadence.com/doc/user-manual/getting-started/command-line-options.html](https://www.cadence.com/doc/user-manual/getting-started/command-line-options.html)
- [https://github.com/pointwise/GlyphClientPython](https://github.com/pointwise/GlyphClientPython)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.glf` | [hello.glf](hello.glf) created; verification pending |
