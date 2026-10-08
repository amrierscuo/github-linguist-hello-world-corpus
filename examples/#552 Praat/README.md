# #552 Praat

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Eseguire uno script Praat e scrivere Hello, World! nella finestra Info/stdout batch.

audience$ è una stringa Praat. writeInfoLine usa il comando nativo; il runtime batch restituisce output UTF16LE, decodificato nel log e confrontato con il saluto. Nessun audio viene registrato o riprodotto.

## Toolchain e riproduzione

Praat7.0.02 ufficiale Windows x64v1

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
Praat.exe --run hello.praat
```

## Risultato atteso e stato

Hello, World! seguito da newline; exit0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://www.fon.hum.uva.nl/praat/manual/Scripting.html
- https://github.com/praat/praat/releases/tag/v7.0.02

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.praat` | [hello.praat](hello.praat) verificato |
