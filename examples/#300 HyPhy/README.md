# #300 HyPhy

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Interpretare un batch HyPhy HBL e stampare il saluto tramite fprintf(stdout,...).

Il file .bf è HyPhy Batch Language, distinto da Brainfuck. greeting è un’espressione stringa e fprintf emette il valore. Il programma non richiede dati genetici, analisi di sequenze o calcolo statistico; il log prova il runtime originale.

## Toolchain e riproduzione

HyPhy2.5.59(MP), binario Linux x86SSE4 e pacchetti Ubuntu2.5.59+dfsg-1build3

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
hyphy hello.bf
```

## Risultato atteso e stato

stdout esattamente Hello, World! seguito da newline; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://hyphy.org/
- https://github.com/veg/hyphy
- https://raw.githubusercontent.com/veg/hyphy/master/tests/hbltests/RegressionTesting/LocalReferenceBug.bf

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bf` | [hello.bf](hello.bf) verificato |
