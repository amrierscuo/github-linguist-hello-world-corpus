# 0485 — OCaml: `.mll`

Ruolo: Specifica ocamllex con regola che riconosce il saluto; include trailer main.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: OCaml 4.14.1. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
ocamllex hello.mll; ocamlc -o hello hello.ml; ./hello
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.mll`: `b451bfd0e67cb81b0a713116e68403f1099cce7cb0990c3b2a2d1ec7d07feac3`

Fonti primarie:

- https://ocaml.org/manual/5.3/lexyacc.html
- https://ocaml.org/manual/5.4/programs.html
