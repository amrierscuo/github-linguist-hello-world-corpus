# 0359 — KiCad Schematic: `.kicad_sym`

Ruolo: Libreria simboli KiCad con proprietà Value del saluto, distinta da schematico.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Required genuine toolchain not available/configured — non disponibile / non verificata. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
KiCad Symbol Editor: aprire/importare hello.kicad_sym
```

Risultato atteso: Simbolo Greeting con Value Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.kicad_sym`: `282187cb51a3956825f982795eadf5d64e709c8945ec917088986323ed03e992`

Fonti primarie:

- https://dev-docs.kicad.org/en/file-formats/sexpr-symbol-lib/
- https://dev-docs.kicad.org/en/file-formats/sexpr-schematic/
- https://docs.kicad.org/7.0/en/eeschema/eeschema.html
