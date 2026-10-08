# 0423 — Max: `.maxproj`

Ruolo: Descriptor progetto Max testuale authored con struttura attestata da un progetto pubblicato dal suo autore: nome saluto e patcher locale. Date fisse illustrative (2000-01-01); non si dichiara export da un Max eseguito.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Cycling ’74 Max 8+. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Max originale: aprire hello.maxproj in directory di lavoro; confermare progetto e hello.maxpat locale top-level; eseguire patcher e leggere console.
```

Risultato atteso: Progetto Hello, World! con patcher del saluto; schema/loading originale pendenti.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.
- Max non disponibile: JSON è redatto secondo una struttura di progetto attestata ma lo schema applicativo e il caricamento del progetto non sono stati verificati.

SHA-256 dei file della variante:

- `hello.maxpat`: `0891aa513d9e3cedeb7b8d09e835264e3e52aa063c028c4627230767117e8540`
- `hello.maxproj`: `613a5748c7b92e814d820b79bcdc68e28914abde73e883de3d26400bbdd3dc05`

Fonti primarie:

- https://docs.cycling74.com/userguide/projects/
- https://github.com/rennyhyde/HARD2500/blob/main/HARD_2500.maxproj
- https://docs.cycling74.com/reference/message/
- https://docs.cycling74.com/reference/print/
