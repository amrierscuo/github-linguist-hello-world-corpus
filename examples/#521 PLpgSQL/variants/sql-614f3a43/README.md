# 0521 — PLpgSQL: `.sql`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#521 PLpgSQL/hello.pgsql.

Toolchain richiesta: Authentic PostgreSQL PL/pgSQL engine — psql (PostgreSQL) 16.15 (Ubuntu 16.15-0ubuntu0.24.04.1). La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.sql; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: Il risultato conforme contiene Hello, World!, secondo l’ambito descritto.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.sql`: `9e12a294843a6e9e7e44b92a6d9f4cc29d173f9338b49929cb17374770e92851`

Fonti primarie:

- https://www.postgresql.org/docs/16/plpgsql.html
