# 0503 — OpenEdge ABL: `.w`

Ruolo: Window procedure ABL: crea un widget window locale con titolo del saluto, distrutto a fine test.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Progress OpenEdge ABL. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
OpenEdge GUI: RUN hello.w in sessione locale di test; chiudere la finestra
```

Risultato atteso: Finestra con titolo Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.w`: `d6dcfdd375626f4cf5acd83d58df8e33acd149000bd6a11f271142f8d3d0f2ca`

Fonti primarie:

- https://documentation.progress.com/output/ua/OpenEdge_latest/gsins/openedge-file-types.html
- https://docs.progress.com/bundle/abl-reference/page/MESSAGE-statement.html
