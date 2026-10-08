# 0349 — Just: `.just`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#349 Just/justfile.

Toolchain richiesta: Official Just recipe parser and runner — just 1.58.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.just; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: Ricetta elencata; exit 0; saluto esatto.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.just`: `23a4dece0400d8027f0cf079b6e0f3473054c6ff51f667a53695e59bb0d2e941`

Fonti primarie:

- https://just.systems/man/en/
- https://github.com/casey/just
