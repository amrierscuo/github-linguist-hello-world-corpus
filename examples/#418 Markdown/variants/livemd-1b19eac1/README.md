# 0418 — Markdown: `.livemd`

Ruolo: Notebook Livebook Markdown con sezione e cella Elixir eseguibile, non output registrato inventato.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Python 3.13.9 + markdown-it-py 4.2.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Livebook: importare hello.livemd e valutare la cella
```

Risultato atteso: Hello, World! nella cella

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.livemd`: `7762dbb562980095688ba0cb1a3e2d32a94456bf9d09678c8ae8568649b3d676`

Fonti primarie:

- https://github.com/livebook-dev/livebook
- https://spec.commonmark.org/0.31.2/
- https://github.com/executablebooks/markdown-it-py
