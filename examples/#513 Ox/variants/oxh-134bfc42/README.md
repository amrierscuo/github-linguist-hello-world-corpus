# 0513 — Ox: `.oxh`

Ruolo: Header Ox con dichiarazione esterna della funzione Greeting; implementazione distinta.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Ox Console/OxMetrics e oxstd. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Ox Console: compilare hello.ox che include hello.oxh
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.ox`: `7376e53d2ed72340807d4a1624eae3d19eb4fc5128a8b367370bbaae6b763c4e`
- `hello.oxh`: `7ef5b8be8dfe030114a21a1b9af0459e6ef1017e197027fb3ef474299a53d201`

Fonti primarie:

- https://www.doornik.com/ox/
- https://www.doornik.com/ox/ox.html
