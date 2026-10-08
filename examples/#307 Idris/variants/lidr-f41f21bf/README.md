# 0307 — Idris: `.lidr`

Ruolo: Sorgente Idris literate in stile Bird: codice preceduto da >.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Idris; scegliere/registrare una versione compatibile con .idr. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
idris hello.lidr -o hello; ./hello
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.lidr`: `de05f69112435185e1513371061d8ec0fd732209d7264f1e341d243960372b70`

Fonti primarie:

- https://docs.idris-lang.org/en/latest/tutorial/miscellany.html#literate-programming
- https://docs.idris-lang.org/en/latest/tutorial/introduction.html
- https://docs.idris-lang.org/en/latest/tutorial/starting.html
