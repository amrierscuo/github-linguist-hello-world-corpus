# 0636 — SQL — `.udf`

UDF scalare T-SQL per SQL Server in database di prova.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.udf`.

Controllo previsto, dalla cartella della variante:

```text
sqlcmd -i hello.udf (isolated test database)
```

Risultato atteso: funzione restituisce Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://learn.microsoft.com/en-us/sql/t-sql/statements/create-function-transact-sql](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-function-transact-sql)
