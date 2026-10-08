# 0485 — OCaml: `.mly`

Ruolo: Grammatica ocamlyacc con token HELLO e funzione che restituisce il saluto.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: OCaml 4.14.1. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
ocamlyacc hello.mly; ocamlc -c hello.mli; ocamlc -c hello.ml; ocamlc -o driver hello.cmo driver.ml; ./driver
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `driver.ml`: `e6f6c8a85d4d80140be528bd622b6db2b0c82d9aa5079aedf2b10c63b2bf95f7`
- `hello.mly`: `997a0f330e10d8004df0b38df1fcbb1616fedabfcd089dfa3bfafa993f1e465e`

Fonti primarie:

- https://ocaml.org/manual/5.3/lexyacc.html
- https://ocaml.org/manual/5.4/programs.html
