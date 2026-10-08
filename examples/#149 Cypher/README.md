# #149 Cypher

Voce canonica e ordine del `reference/languages.yml` del corpus. I sorgenti e fixture sono originali; eventuali dump/bundle provengono dagli strumenti indicati.

## Obiettivo

Eseguire una query Cypher che restituisce una sola riga greeting = Hello, World!.

La query usa RETURN, concatenazione di stringhe e alias. verify.py apre un database locale temporaneo nella copia di lavoro, esegue hello.cypher con il motore Kuzu e controlla colonne e righe. La verifica riguarda il dialetto Cypher implementato da Kuzu; non richiede un server Neo4j o connessioni esterne.

## Toolchain e riproduzione

Kuzu 0.11.3, motore Cypher originale via Python 3.13.9

Comandi nella cartella dell’esempio con la toolchain disponibile nel PATH. Usare una copia temporanea: database, oggetti, audio e altri output di prova non appartengono al corpus.

```text
python verify.py
```

## Risultato atteso e stato

PASS: one row, greeting = Hello, World!; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra versioni e provenienza, SHA-256 dei sorgenti, comandi effettivi, exit, stdout e stderr normalizzati.

## Fonti primarie

- https://neo4j.com/docs/cypher-manual/4.4/clauses/return/
- https://kuzudb.github.io/docs/client-apis/python/
- https://github.com/kuzudb/kuzu

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cyp` | [hello.cyp](variants/ext-cyp-2e637970/hello.cyp) creato, verifiche pendenti |
| `.cypher` | [hello.cypher](hello.cypher) verificato |
