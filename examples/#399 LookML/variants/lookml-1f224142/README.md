# 0399 — LookML: `.lookml`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#399 LookML/hello.view.lkml.

Toolchain richiesta: Community lkml 1.3.7 genuine LookML parser; SQLite 3.51.0; Python 3.13.9. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.lookml; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: Parser accetta view/derived_table/dimension; SQL restituisce il saluto; Looker deve validare e interrogare la dimensione.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.lookml`: `59870c7955ce0f2e9462e464fc8a32eeeadca43bd96782da82e1b38ce43d262e`
- `requirements.txt`: `d74b32eaaf2c09fc4650a0d2d80fa9007320a4e288989534904bfe613a74ec7f`
- `verify.py`: `2c06ea75bec9133fc326974e2c7ab6c4031805d966b5be52c520d71884c32b79`

Fonti primarie:

- https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table
- https://github.com/joshtemple/lkml
