# #640 STAR

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Analizzare un blocco STAR e leggere il dato Hello, World!.

Questo esempio STAR usa esclusivamente il sottoinsieme scalare compatibile con CIF. Gemmi legge il blocco e decodifica la stringa; non si dichiara verifica di tutti i costrutti STAR.

## Toolchain e riproduzione

Gemmi0.7.5 originale

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
python verify.py
```

## Risultato atteso e stato

Il valore _greeting è Hello, World!.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://www.iucr.org/__data/iucr/cif/standard/cifstd4.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.star` | [hello.star](hello.star) verificato |
