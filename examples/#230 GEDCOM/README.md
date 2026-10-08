# #230 GEDCOM

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Analizzare un GEDCOM 5.5.1 e recuperare una NOTE con valore Hello, World!.

HEAD dichiara versione, formato e UTF-8; la NOTE top-level ha un identificatore e TRLR conclude il documento. La verifica usa Parser.parse_file(strict=True) della libreria originale e controlla la NOTE ottenuta. Non è una validazione completa di tutte le regole genealogiche dello standard.

## Toolchain e riproduzione

python-gedcom 1.1.0, CPython 3.13.9

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
python verify.py
```

## Risultato atteso e stato

PASS: GEDCOM NOTE = Hello, World!; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://gedcom.io/specifications/ged551.pdf
- https://github.com/nickreynke/python-gedcom

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ged` | [hello.ged](hello.ged) verificato |
