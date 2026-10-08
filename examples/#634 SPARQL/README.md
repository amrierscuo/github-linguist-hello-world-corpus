# #634 SPARQL

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Valutare una query SPARQL che concatena Hello, e World!.

Query SPARQL1.1 su grafo vuoto; il driver usa parser/evaluatore RDFlib e controlla un’unica soluzione.

## Toolchain e riproduzione

RDFlib7.6.0 originale

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
python verify.py
```

## Risultato atteso e stato

Un’unica riga con greeting = Hello, World!.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://www.w3.org/TR/sparql11-query/#func-concat

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.sparql` | [hello.sparql](variants/sparql-6c620153/hello.sparql) creato, verifiche pendenti |
| `.rq` | [hello.rq](hello.rq) verificato |
