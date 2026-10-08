# #553 Prisma

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Validare Prisma Schema Language con modello Greeting e default Hello, World!.

La schema definisce un datasource SQLite e un modello Greeting il cui campo text ha default esplicito. Il validator originale controlla sintassi e schema; non viene attribuita una inserzione SQL non eseguita.

## Toolchain e riproduzione

Prisma7.10.0 ufficiale, Node22.20.0

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
prisma validate --schema hello.prisma
```

## Risultato atteso e stato

Schema valida, modello Greeting con default Hello, World!.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: no.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

Impedimenti: Client/runtime di inserzione nel database non preparato; semantica del default pendente.

## Fonti primarie

- https://docs.prisma.io/docs/cli/v7/validate
- https://www.prisma.io/docs/orm/prisma-schema/data-model/models

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.prisma` | [hello.prisma](hello.prisma) sintassi verificata |
