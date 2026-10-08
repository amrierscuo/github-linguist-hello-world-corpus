# 0357 — KiCad Layout: `.kicad_wks`

Ruolo: Drawing sheet KiCad con elemento tbtext del saluto; non scheda PCB.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Required genuine toolchain not available/configured — non disponibile / non verificata. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
KiCad Drawing Sheet Editor: aprire hello.kicad_wks
```

Risultato atteso: Hello, World! nel foglio

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.kicad_wks`: `a3a6e250bf2fccd2fb3bfc46564e7e4bfc5e9eed7122f40163e79b40673bf75f`

Fonti primarie:

- https://dev-docs.kicad.org/en/file-formats/sexpr-wks/
- https://docs.kicad.org/8.0/en/pl_editor/pl_editor.html
- https://dev-docs.kicad.org/en/file-formats/sexpr-pcb/
- https://docs.kicad.org/7.0/en/pcbnew/pcbnew.html
