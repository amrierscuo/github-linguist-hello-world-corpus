# #636 SQL

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Eseguire SQL e restituire il saluto Hello, World!.

Dialetto SQLite dichiarato; SELECT viene realmente analizzato ed eseguito su database in memoria.

## Toolchain e riproduzione

SQLite3 originale tramite sqlite3 della libreria standard Python; versione nel log

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
python verify.py
```

## Risultato atteso e stato

Una riga, colonna greeting, valore Hello, World!.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://www.sqlite.org/lang_select.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.sql` | [hello.sql](hello.sql) verificato |
| `.ddl` | [hello.ddl](variants/ddl-8bc7bf69/hello.ddl) creato, verifiche pendenti |
| `.inc` | [hello.inc](variants/inc-dd126fb7/hello.inc) creato, verifiche pendenti |
| `.mysql` | [hello.mysql](variants/mysql-94d2dcda/hello.mysql) creato, verifiche pendenti |
| `.prc` | [hello.prc](variants/prc-8feafefc/hello.prc) creato, verifiche pendenti |
| `.tab` | [hello.tab](variants/tab-97c85d6e/hello.tab) creato, verifiche pendenti |
| `.udf` | [hello.udf](variants/udf-94d3d68a/hello.udf) creato, verifiche pendenti |
| `.viw` | [hello.viw](variants/viw-71592285/hello.viw) creato, verifiche pendenti |
