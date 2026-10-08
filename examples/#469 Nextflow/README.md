# #469 Nextflow

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Eseguire un workflow locale Nextflow che produce Hello, World!.

Il process GREETING emette stdout dalla propria task Bash; workflow connette il canale a view. Il sorgente è una pipeline DSL2, distinta dallo script della singola task.

## Toolchain e riproduzione

NextflowDSL2, Java21 e Bash; versioni effettive da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
nextflow run hello.nf
```

## Risultato atteso e stato

Hello, World! seguito da newline; exit0.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Runtime Nextflow e dipendenze Java non preparati; pipeline pendente.

## Fonti primarie

- https://nextflow.io/docs/latest/script.html
- https://nextflow.io/docs/latest/process.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.nf` | [hello.nf](hello.nf) creato, verifiche pendenti |
