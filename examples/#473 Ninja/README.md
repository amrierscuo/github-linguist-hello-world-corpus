# #473 Ninja

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Eseguire un grafo Ninja che genera un file con Hello, World!.

Il file .ninja definisce rule, dipendenza esplicita e target default. Ninja originale interpreta il grafo e avvia la fixture Python; il contenuto del file prodotto viene confrontato esattamente.

## Toolchain e riproduzione

Ninja1.11.1, Python3 della fixture

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
ninja -f hello.ninja
```

## Risultato atteso e stato

greeting.txt contiene i13byte Hello, World!; exit0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://ninja-build.org/manual.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ninja` | [hello.ninja](hello.ninja) verificato |
