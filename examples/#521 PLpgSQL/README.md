# #521 PLpgSQL

Voce canonica `PLpgSQL`, tipo `programming`, language_id `274`.

Creare una funzione PL/pgSQL temporanea parametrica e verificarne due risultati.

## Toolchain e riproduzione

Authentic PostgreSQL PL/pgSQL engine — psql (PostgreSQL) 16.15 (Ubuntu 16.15-0ubuntu0.24.04.1). Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

PostgreSQL 16.15 con ruolo locale e database di prova; la funzione vive in pg_temp e la transazione termina con ROLLBACK.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
psql -X -q -A -t -d postgres -v ON_ERROR_STOP=1 -f hello.pgsql
```

Risultato atteso: Il risultato conforme contiene Hello, World!, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

La prova autentica esegue CREATE FUNCTION, SELECT World, controllo Reader e rollback. Nessun oggetto persistente.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.postgresql.org/docs/16/plpgsql.html](https://www.postgresql.org/docs/16/plpgsql.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pgsql` | [hello.pgsql](hello.pgsql) verificato |
| `.sql` | [hello.sql](variants/sql-614f3a43/hello.sql) creato, verifiche pendenti |
