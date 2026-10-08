# 0637 — SQLPL — `.sql`

Variante testuale dello stesso formato, con suffisso canonico .sql.

Provenienza: copia del file originale `examples/#637 SQLPL/hello.db2`.

Artefatto principale: `hello.sql`.

Controllo previsto, dalla cartella della variante:

```text
db2 -td@ -vf hello.sql
```

Risultato atteso: Il parametro OUT greeting vale Hello, World! dopo CALL corpus_greeting(?)..

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://www.ibm.com/docs/en/db2-for-zos/12.0.0?topic=procedures-sql-procedure-body](https://www.ibm.com/docs/en/db2-for-zos/12.0.0?topic=procedures-sql-procedure-body)
