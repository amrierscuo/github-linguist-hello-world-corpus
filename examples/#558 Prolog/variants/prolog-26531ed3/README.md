# 0558 — Prolog: `.prolog`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#558 Prolog/hello.pl.

Toolchain richiesta: SWI-Prolog9.0.4 ufficiale Ubuntu. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.prolog; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: Hello, World! seguito da newline; exit0.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.prolog`: `087467ce1818250c527ca4d9e1e9e661dd740297135a4c1d59e6536a0f74f3c0`

Fonti primarie:

- https://www.swi-prolog.org/pldoc/doc_for?object=atomic_list_concat/2
- https://www.swi-prolog.org/pldoc/doc_for?object=initialization/2
