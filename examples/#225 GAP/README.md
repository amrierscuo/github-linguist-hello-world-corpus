# #225 GAP

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Valutare un’espressione GAP, stamparla e terminare con successo.

Concatenation costruisce greeting, Print produce il saluto e QUIT_GAP(0) conclude il processo. La verifica esegue il binario GAP autentico con la libreria di base isolata e senza package opzionali.

## Toolchain e riproduzione

GAP 4.12.1, pacchetti Ubuntu 4.12.1-2build2

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
gap -q -A -T hello.g
```

## Risultato atteso e stato

stdout esattamente Hello, World! seguito da newline; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://docs.gap-system.org/doc/tut/manual.pdf
- https://www.gap-system.org/

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.g` | [hello.g](hello.g), [consumer.g](variants/ext-gd-2e6764/consumer.g), [consumer.g](variants/ext-gi-2e6769/consumer.g) creato, verifiche pendenti |
| `.gap` | [hello.gap](variants/ext-gap-2e676170/hello.gap) creato, verifiche pendenti |
| `.gd` | [hello.gd](variants/ext-gd-2e6764/hello.gd) creato, verifiche pendenti |
| `.gi` | [hello.gi](variants/ext-gi-2e6769/hello.gi) creato, verifiche pendenti |
| `.tst` | [hello.tst](variants/ext-tst-2e747374/hello.tst) creato, verifiche pendenti |
