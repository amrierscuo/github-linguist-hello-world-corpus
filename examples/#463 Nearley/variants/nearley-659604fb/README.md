# 0463 — Nearley: `.nearley`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#463 Nearley/hello.ne.

Toolchain richiesta: Nearley2.20.1, Node22.20.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
nearleyc hello.nearley -o hello.js; node verify.js
```

Risultato atteso: Hello, World! seguito da newline; exit0.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.nearley`: `3a88908ad98babe930774529f396d9e79b5d6e41f37dc2ad6f91f13d6851901a`
- `verify.js`: `7093458dba252c87d7ac4fe1360c804159d75dc3b076db78243a006561819fc7`

Fonti primarie:

- https://nearley.js.org/docs/grammar
- https://nearley.js.org/docs/parser
