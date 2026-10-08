# #463 Nearley

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Compilare una grammatica Nearley e riconoscere Hello, World!.

Il compiler nearleyc genera il parser dalla grammatica originale; il driver alimenta il parser Nearley con il saluto e confronta l’unico risultato. hello.js viene generato soltanto nella copia in work.

## Toolchain e riproduzione

Nearley2.20.1, Node22.20.0

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
nearleyc hello.ne -o hello.js
```

```text
node verify.js
```

## Risultato atteso e stato

Hello, World! seguito da newline; exit0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://nearley.js.org/docs/grammar
- https://nearley.js.org/docs/parser

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ne` | [hello.ne](hello.ne) verificato |
| `.nearley` | [hello.nearley](variants/nearley-659604fb/hello.nearley) creato, verifiche pendenti |
