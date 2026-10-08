# 0636 — SQL — `.mysql`

Query MySQL; la funzione CONCAT richiede il dialetto appropriato.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.mysql`.

Controllo previsto, dalla cartella della variante:

```text
mysql --batch --skip-column-names < hello.mysql
```

Risultato atteso: Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://dev.mysql.com/doc/refman/8.4/en/string-functions.html#function_concat](https://dev.mysql.com/doc/refman/8.4/en/string-functions.html#function_concat)
