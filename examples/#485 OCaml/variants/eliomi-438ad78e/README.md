# 0485 — OCaml: `.eliomi`

Ruolo: Interfaccia Eliom lato server; implementazione corrispondente inclusa.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: OCaml 4.14.1. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Eliom originale: compilare greeting.eliomi e greeting.eliom lato server
```

Risultato atteso: Interfaccia server con greeting stringa

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `greeting.eliom`: `c8aec92538be01f759c17a68e8eafe4cffec465ccb682b8c2da08204b53dc3ef`
- `greeting.eliomi`: `9a65e001a8ddb6bff30297a3bb312f4aac0c4dd4913170e2fbc5edb1429fb058`

Fonti primarie:

- https://ocsigen.org/eliom/latest/manual/clientserver-language
- https://ocaml.org/manual/5.4/programs.html
