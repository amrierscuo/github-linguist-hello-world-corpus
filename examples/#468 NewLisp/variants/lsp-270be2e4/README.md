# 0468 — NewLisp: `.lsp`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#468 NewLisp/hello.nl.

Toolchain richiesta: newLISP10.7.5 Linux ufficiale Ubuntu. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.lsp; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: Hello, World! seguito da newline; exit0.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.lsp`: `5fd420fcf931cfee86b0d3736f9b709ec15b8c07e22e4ca9220c5d7d04e34d10`

Fonti primarie:

- https://www.newlisp.org/downloads/newlisp_manual.html
