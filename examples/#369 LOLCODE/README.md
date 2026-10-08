# #369 LOLCODE

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Interpretare LOLCODE1.2 e stampare Hello, World!.

Il programma dichiara due variabili, usa SMOOSH per la concatenazione e VISIBLE per l’output. Il log identifica distribuzione sorgente, hash dell’interprete e versione effettiva.

## Toolchain e riproduzione

lci0.11.2 originale justinmeza, branch future; GCC e librerie readline/ncurses

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
lci hello.lol
```

## Risultato atteso e stato

stdout esattamente Hello, World! seguito da newline; exit0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://lolcode.org/
- https://github.com/justinmeza/lci

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.lol` | [hello.lol](hello.lol) verificato |
