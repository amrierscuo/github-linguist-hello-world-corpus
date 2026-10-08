# #701 TSPLIB data

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Analizzare un problema TSP originale e leggere il metadato Hello, World!.

Tre città, distanze EUC_2D e COMMENT contenente il saluto. Il driver usa il parser autentico, controlla i nodi e una distanza, poi legge COMMENT; non risolve un TSP.

## Toolchain e riproduzione

tsplib95 0.7.1 originale

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
python verify.py
```

## Risultato atteso e stato

COMMENT = Hello, World!, tre nodi e distanza1 fra nodi1 e2.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://tsplib95.readthedocs.io/en/stable/pages/usage.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.tsp` | [hello.tsp](hello.tsp) verificato |
