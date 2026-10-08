# 0485 — OCaml: `.eliom`

Ruolo: Modulo Eliom server/client delimitato: funzione server-side senza avviare rete.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: OCaml 4.14.1. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Eliom originale con ppx_eliom: compilare il modulo lato server
```

Risultato atteso: Hello, World! nel log server locale

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.eliom`: `35c4d4d155d8ba4273d15f2480275c54c5741f160cfa881064b09792a55224f7`

Fonti primarie:

- https://ocsigen.org/eliom/latest/manual/clientserver-language
- https://ocaml.org/manual/5.4/programs.html
