# 0636 — SQL — `.ddl`

SQL DDL SQLite con tabella e dato originale.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.ddl`.

Controllo previsto, dalla cartella della variante:

```text
sqlite3 :memory: < hello.ddl
```

Risultato atteso: Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://www.sqlite.org/lang_select.html](https://www.sqlite.org/lang_select.html)
