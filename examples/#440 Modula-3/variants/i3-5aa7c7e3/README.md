# 0440 — Modula-3: `.i3`

Ruolo: Interfaccia Modula-3 con PROCEDURE Greet, implementazione e main distinti.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Critical Mass Modula-3 cm3 e libm3. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
cm3 con m3makefile del fixture; ./hello
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `Greeting.i3`: `bc7eacb2d3e9100448f2f75d63309ba4f067d9860440007273b8d352ba4f2c05`
- `Greeting.m3`: `37760a248cbde0a43c904f2d08d1dec4b265c5e6f318b4fddd8e4ce9de0aae8e`
- `Main.m3`: `bb40e3263566a42aadb7b4f5c05eb633e0e7152e2d12bf552ffb99645d7f5a39`
- `m3makefile`: `b19e7d91dd4cf15d0e3dc3fcc8dfc3d18fc76ed139648ea82e163d167afe337c`

Fonti primarie:

- https://www.cs.purdue.edu/homes/hosking/m3/reference/complete/m3-defn-complete.pdf
- https://github.com/modula3/cm3
