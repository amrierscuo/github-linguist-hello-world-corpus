# #703 TSV

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Analizzare una tabella TSV e leggere il valore Hello, World!.

Tabella con header key e value; csv.DictReader usa realmente il delimitatore TAB.

## Toolchain e riproduzione

Python csv originale; versione nel log

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
python verify.py
```

## Risultato atteso e stato

Una riga dati, chiave greeting, valore Hello, World!.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://docs.python.org/3/library/csv.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.tsv` | [hello.tsv](hello.tsv) verificato |
| `.vcf` | [hello.vcf](variants/vcf-96d2ee95/hello.vcf) creato, verifiche pendenti |
