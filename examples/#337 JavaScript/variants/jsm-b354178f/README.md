# 0337 — JavaScript: `.jsm`

Ruolo: Modulo Mozilla JSM legacy con export dichiarato; nessun console.log top-level.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Node.js 22.20.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Firefox legacy compatibile: importare il modulo JSM e leggere greeting
```

Risultato atteso: Hello, World! nel log/valore/risposta o geometria secondo il ruolo; PAC restituisce DIRECT senza rete.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.jsm`: `2fe55cf92a1eca85af71e6940601cc9dea7409fa2b2df50708c8ac0c3c16b4a4`

Fonti primarie:

- https://firefox-source-docs.mozilla.org/dom/scriptloader/jsm_importer.html
- https://nodejs.org/api/console.html#consolelogdata-args
