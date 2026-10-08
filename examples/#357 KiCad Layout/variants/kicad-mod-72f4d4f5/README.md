# 0357 — KiCad Layout: `.kicad_mod`

Ruolo: Footprint di libreria con fp_text user del saluto, distinto da scheda PCB.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Required genuine toolchain not available/configured — non disponibile / non verificata. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
KiCad Footprint Editor: importare hello.kicad_mod e visualizzare il testo
```

Risultato atteso: Hello, World! sul silkscreen del footprint

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.kicad_mod`: `9b2cc5fd1f5cf072bb7cf5e956c162b79e6237ed9918294560872e982b438a74`

Fonti primarie:

- https://dev-docs.kicad.org/en/file-formats/sexpr-footprint/
- https://dev-docs.kicad.org/en/file-formats/sexpr-pcb/
- https://docs.kicad.org/7.0/en/pcbnew/pcbnew.html
