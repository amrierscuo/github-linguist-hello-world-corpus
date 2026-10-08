# 0485 — OCaml: `.mli`

Ruolo: Interfaccia OCaml dichiarativa: val greeting, implementazione e main separati.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: OCaml 4.14.1. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
ocamlc -c greeting.mli; ocamlc -c greeting.ml; ocamlc -o hello greeting.cmo main.ml; ./hello
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `greeting.ml`: `9f86810393a29016ca792ebe4513e9693808a6d66980cd4dc18a88b9abab1f94`
- `greeting.mli`: `3540feaa3df9e3613e5afe11b348a90f7b42e21978d8303a29075cfa14e12b9a`
- `main.ml`: `70213b9bc2df66f4f978734722cac6abf3e7865a5f72422b78ce310e09745724`

Fonti primarie:

- https://ocaml.org/manual/5.3/moduleexamples.html
- https://ocaml.org/manual/5.4/programs.html
