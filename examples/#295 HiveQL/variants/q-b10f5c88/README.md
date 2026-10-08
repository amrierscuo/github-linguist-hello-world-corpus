# 0295 — HiveQL: `.q`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#295 HiveQL/check.py.

Toolchain richiesta: SQLGlot30.21.0 parser Hive; Apache Hive per query runtime non preparato. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.q; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: Query accettata, una riga greeting con valore Hello, World!.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.hql`: `a5e3aa59529003186d0f7666d6387cefdae6fda7380a1838406f2bf7b6e47952`
- `hello.q`: `4b5b0f638205786e633d8d9cd1c4a0b2421c547d626e46ffbaf71946db0515b0`

Fonti primarie:

- https://cwiki.apache.org/confluence/spaces/Hive/pages/27362046/LanguageManual+UDF
- https://github.com/tobymao/sqlglot
