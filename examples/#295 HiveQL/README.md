# #295 HiveQL

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Analizzare HiveQL e, con un motore Hive, restituire la colonna greeting = Hello, World!.

Il parser originale SQLGlot viene invocato con read=hive e rigenera la query nel medesimo dialetto. Questo controlla il parsing HiveQL; l’esecuzione Apache Hive della funzione concat non è stata effettuata. Non si equipara un risultato SQLite alla semantica Hive.

## Toolchain e riproduzione

SQLGlot30.21.0 parser Hive; Apache Hive per query runtime non preparato

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
python check.py
```

```text
Con Hive disponibile: hive -f hello.hql
```

## Risultato atteso e stato

Query accettata, una riga greeting con valore Hello, World!.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: no.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

Impedimenti: Apache Hive e il relativo runtime query non preparati; semantica pendente.

## Fonti primarie

- https://cwiki.apache.org/confluence/spaces/Hive/pages/27362046/LanguageManual+UDF
- https://github.com/tobymao/sqlglot

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.q` | [hello.q](variants/q-b10f5c88/hello.q) creato, verifiche pendenti |
| `.hql` | [hello.hql](hello.hql), [hello.hql](variants/q-b10f5c88/hello.hql) creato, verifiche pendenti |
