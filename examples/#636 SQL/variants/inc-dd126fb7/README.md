# 0636 — SQL — `.inc`

Fragment SQL includibile che conserva la query originale.

Provenienza: copia del file originale `examples/#636 SQL/hello.sql`.

Artefatto principale: `hello.inc`.

Controllo previsto, dalla cartella della variante:

```text
sqlite3 :memory: < hello.inc
```

Risultato atteso: Una riga, colonna greeting, valore Hello, World!..

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://www.sqlite.org/lang_select.html](https://www.sqlite.org/lang_select.html)
