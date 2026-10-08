# #718 TextGrid

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Analizzare TextGrid e leggere il saluto dall’etichetta del primo intervallo.

TextGrid originale con un IntervalTier da0 a1 secondo. Praat legge il formato e il driver interroga la label: non serve un file audio.

## Toolchain e riproduzione

Praat7.0.02 originale

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
praat --run verify.praat
```

## Risultato atteso e stato

Label = Hello, World!, stampata dal runtime.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://www.fon.hum.uva.nl/praat/manual/TextGrid_file_formats.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.TextGrid` | [hello.TextGrid](hello.TextGrid) verificato |
