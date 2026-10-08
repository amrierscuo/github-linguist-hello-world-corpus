# 0533 — Pic: `.chem`

Ruolo: DSL chem per anello benzene e inserimento Pic documentato di una etichetta; distinto dal blocco Pic .PS.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Genuine GNU Pic and groff ASCII renderer — GNU pic (groff) version 1.23.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
chem hello.chem | groff -p -Tps > hello.ps
```

Risultato atteso: Diagramma chimico etichettato Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.
- La combinazione chem/pic deve essere ancora interpretata dal tool originale; nessuna verifica viene ereditata da Pic.

SHA-256 dei file della variante:

- `hello.chem`: `808dc33a8c6f4659d1393b523fef3f8764a3b23fc5edc1551e3ae3a411b60c9b`

Fonti primarie:

- https://www.gnu.org/software/groff/manual/groff-man-pages.pdf
- https://www.gnu.org/software/groff/manual/groff.html#Pictures
