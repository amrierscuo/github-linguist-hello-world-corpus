# 0149 Cypher — variante `.cyp`

Ruolo: Alias testuale dello stesso formato e dello stesso programma/dataset del modello originale.

Tipo variante: **alias**. Copia byte-identica di examples/#149 Cypher/hello.cypher

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Cypher runtime locale: eseguire il file hello.cyp e confrontare la colonna di risultato originale.
```

Risultato atteso: PASS: one row, greeting = Hello, World!; exit 0.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://neo4j.com/docs/cypher-manual/4.4/clauses/return/](https://neo4j.com/docs/cypher-manual/4.4/clauses/return/)
- [https://kuzudb.github.io/docs/client-apis/python/](https://kuzudb.github.io/docs/client-apis/python/)
- [https://github.com/kuzudb/kuzu](https://github.com/kuzudb/kuzu)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
