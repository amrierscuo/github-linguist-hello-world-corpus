# 0337 — JavaScript: `.jake`

Ruolo: Task Jake DSL, non main JavaScript generico.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Node.js 22.20.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
jake -f hello.jake hello
```

Risultato atteso: Hello, World! nel log/valore/risposta o geometria secondo il ruolo; PAC restituisce DIRECT senza rete.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.jake`: `dfdc8e6f6117faa5f8b3e8df876bf2e2c573aded23959c5797e8a6937e2ec99e`

Fonti primarie:

- https://jakejs.com/
- https://nodejs.org/api/console.html#consolelogdata-args
