# #702 TSQL

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Eseguire TSQL e restituire Hello, World! da SELECT.

La variabile Unicode nvarchar viene concatenata con l’operatore + del dialetto TSQL.

## Toolchain e riproduzione

Microsoft SQL Server TSQL, versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
sqlcmd -i hello.sql
```

## Risultato atteso e stato

Una riga, greeting = Hello, World!.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: SQL Server/sqlcmd non disponibili; parser ed esecuzione pendenti.

## Fonti primarie

- https://learn.microsoft.com/en-us/sql/t-sql/language-elements/string-operators-transact-sql?view=sql-server-2017

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.sql` | [hello.sql](hello.sql) creato, verifiche pendenti |
