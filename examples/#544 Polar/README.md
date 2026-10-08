# #544 Polar

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Caricare una regola Polar e ricavare il binding message=Hello, World!.

La regola greeting è un fatto Polar originale. Oso carica la policy e il driver interroga il motore con Variable(message), confrontando il valore del binding. Non è una policy di autorizzazione applicata a risorse; l’avviso Oso per assenza di allow è registrato.

## Toolchain e riproduzione

Oso/Polar0.27.3, CFFI1.17.1, Python3.12 Linux

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
python3 verify.py
```

## Risultato atteso e stato

Una soluzione message=Hello, World!, emessa dal driver; exit0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://github.com/osohq/oso
- https://docs.oso.dev/ruby/getting-started/application/model.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.polar` | [hello.polar](hello.polar) verificato |
