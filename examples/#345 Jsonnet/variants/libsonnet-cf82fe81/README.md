# 0345 — Jsonnet: `.libsonnet`

Ruolo: Libreria Jsonnet che esporta una stringa; il fixture importa la libreria.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Official Jsonnet C++ compiler/evaluator — Jsonnet commandline interpreter v0.20.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
jsonnet driver.jsonnet
```

Risultato atteso: "Hello, World!"

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `driver.jsonnet`: `16baeb51f9d910982b6a0617826211ebc5fbe1a9f6bf1d5c3ab59eae351cb009`
- `hello.libsonnet`: `fcebf6eae7df3c1c619fe5211b1bc1e31da633193024f31687f21d786d03cb8b`

Fonti primarie:

- https://jsonnet.org/learning/tutorial.html
- https://jsonnet.org/ref/spec.html
