# #145 Cue Sheet

Voce canonica e ordine del `reference/languages.yml` del corpus. I sorgenti e fixture sono originali; eventuali dump/bundle provengono dagli strumenti indicati.

## Obiettivo

Analizzare un Cue Sheet e recuperare il titolo Hello, World! della traccia audio 01.

hello.cue usa FILE, TRACK, TITLE e INDEX nel formato CDRWIN/CUE sheet. Non è un programma nel linguaggio CUE. La fixture originale genera un secondo di silenzio PCM soltanto nella copia temporanea; cueprint verifica parser e metadata, senza masterizzazione o riproduzione audio.

## Toolchain e riproduzione

cuetools pacchetto 1.4.1-0.2; cueprint dichiara 1.4.0; Python 3.13.9 per fixture

Comandi nella cartella dell’esempio con la toolchain disponibile nel PATH. Usare una copia temporanea: database, oggetti, audio e altri output di prova non appartengono al corpus.

```text
python make_fixture.py
cueprint -i cue -n 1 -t %t hello.cue
```

## Risultato atteso e stato

Titolo estratto esattamente Hello, World!, senza newline aggiunta dal template %t; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra versioni e provenienza, SHA-256 dei sorgenti, comandi effettivi, exit, stdout e stderr normalizzati.

## Fonti primarie

- https://www.gnu.org/software/ccd2cue/manual/html_node/CUE-sheet-format.html
- https://manpages.debian.org/bullseye/cuetools/cueprint.1.en.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cue` | [hello.cue](hello.cue) verificato |
