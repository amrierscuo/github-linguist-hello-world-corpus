# #149 Cypher

The canonical entry and order come from the corpus's `reference/languages.yml`. Sources and fixtures are original; any dumps or bundles come from the stated tools.

## Goal

Run a Cypher query that returns a single greeting line = Hello, World!.

La query usa RETURN, concatenazione di stringhe e alias. verify.py apre un database locale temporaneo nella copia di lavoro, esegue hello.cypher con il motore Kuzu e controlla colonne e righe. La verifica riguarda il dialetto Cypher implementato da Kuzu; non richiede un server Neo4j o connessioni esterne.

## Toolchain and reproduction

Kuzu 0.11.3, motore Cypher originale via Python 3.13.9

Commands in the example folder with the toolchain available in PATH. Use a temporary copy: databases, objects, audio and other test outputs do not belong to the corpus.

```text
python verify.py
```

## Expected result and status

PASS: one row, greeting = Hello, World!; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records versions and provenance, SHA-256 of the source, actual commands, exit, stdout and stderr normalized.

## Primary sources

- https://neo4j.com/docs/cypher-manual/4.4/clauses/return/
- https://kuzudb.github.io/docs/client-apis/python/
- https://github.com/kuzudb/kuzu

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cyp` | [hello.cyp](variants/ext-cyp-2e637970/hello.cyp) created; verification pending |
| `.cypher` | [hello.cypher](hello.cypher) verified |
