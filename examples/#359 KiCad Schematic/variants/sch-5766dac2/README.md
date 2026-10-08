# 0359 — KiCad Schematic: `.sch`

Ruolo: Schematico KiCad legacy v4 testuale con Text Notes, distinto dal moderno s-expression.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Required genuine toolchain not available/configured — non disponibile / non verificata. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
KiCad: aprire hello.sch e controllare il testo prima dell’eventuale conversione
```

Risultato atteso: Nota Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.sch`: `0393945aa8d920e64448988c3c5bb6a4359ebab47f0d5f218be524f76ab78cd5`

Fonti primarie:

- https://dev-docs.kicad.org/en/file-formats/legacy-4-to-6/legacy_file_format_documentation.pdf
- https://dev-docs.kicad.org/en/file-formats/sexpr-schematic/
- https://docs.kicad.org/7.0/en/eeschema/eeschema.html
