# 0485 — OCaml: `.ml4`

Ruolo: Sorgente OCaml standard come input testuale del preprocessore Camlp4; non introduce estensioni di grammatica non documentate.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: OCaml 4.14.1. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
In una directory di lavoro: camlp4o hello.ml4 > hello.ml; ocaml hello.ml
```

Risultato atteso: Hello, World! e LF dopo preprocessamento Camlp4 e interpretazione OCaml.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.
- Camlp4 originale compatibile non predisposto. Nessuna prova viene ereditata dal main OCaml.

SHA-256 dei file della variante:

- `hello.ml4`: `c299624d78a2d8dbde0f49b30bc937b30531ddf5d6e7684eb554a5b4fe51b7d1`

Fonti primarie:

- https://github.com/ocaml/camlp4
- https://caml.inria.fr/pub/old_caml_site/camlp4/tutorial/tutorial003.html
- https://ocaml.org/manual/5.4/programs.html
