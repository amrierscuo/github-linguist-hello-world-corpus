# #295 HiveQL

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Analyze HiveQL and, with a Hive engine, return the greeting column = Hello, World!.

Il parser originale SQLGlot viene invocato con read=hive e rigenera la query nel medesimo dialetto. Questo controlla il parsing HiveQL; l’esecuzione Apache Hive della funzione concat non è stata effettuata. Non si equipara un risultato SQLite alla semantica Hive.

## Toolchain and reproduction

SQLGlot30.21.0 parser Hive; Apache Hive per query runtime non preparato

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
python check.py
```

```text
Con Hive disponibile: hive -f hello.hql
```

## Expected result and status

Query accepted, a greeting line with Hello, World! value.

Artifact created: yes. syntax verified: yes. behavior verified: no.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

Impedimenti: Apache Hive e il relativo runtime query non preparati; semantica pendente.

## Primary sources

- https://cwiki.apache.org/confluence/spaces/Hive/pages/27362046/LanguageManual+UDF
- https://github.com/tobymao/sqlglot

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.q` | [hello.q](variants/q-b10f5c88/hello.q) created; verification pending |
| `.hql` | [hello.hql](hello.hql), [hello.hql](variants/q-b10f5c88/hello.hql) created; verification pending |
