# #521 PLpgSQL

Voce canonica `PLpgSQL`, tipo `programming`, language_id `274`.

Creare una funzione PL/pgSQL temporanea parametrica e verificarne due risultati.

## Toolchain and reproduction

Authentic PostgreSQL PL/pgSQL engine — psql (PostgreSQL) 16.15 (Ubuntu 16.15-0ubuntu0.24.04.1). Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

PostgreSQL 16.15 with local role and test database; the function lives in pg_temp and the transaction ends with ROLLBACK.

Comando/procedura from the directory of the example, unless explicit indications:

```text
psql -X -q -A -t -d postgres -v ON_ERROR_STOP=1 -f hello.pgsql
```

Expected result: The conformed result contains Hello, World!, according to the framework described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

La prova autentica esegue CREATE FUNCTION, SELECT World, controllo Reader e rollback. Nessun oggetto persistente.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.postgresql.org/docs/16/plpgsql.html](https://www.postgresql.org/docs/16/plpgsql.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pgsql` | [hello.pgsql](hello.pgsql) verified |
| `.sql` | [hello.sql](variants/sql-614f3a43/hello.sql) created; verification pending |
