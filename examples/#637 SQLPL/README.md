# #637 SQLPL

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Creare una procedura SQL PL che restituisce Hello, World! in un parametro OUT.

Il terminatore @ distingue la fine del corpo dai suoi punti e virgola. Il saluto viene assegnato al parametro OUT; serve una chiamata successiva per leggerlo.

## Toolchain e riproduzione

IBM Db2 SQL PL, versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
db2 -td@ -vf hello.db2
```

## Risultato atteso e stato

Il parametro OUT greeting vale Hello, World! dopo CALL corpus_greeting(?).

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Db2 di prova non disponibile; creazione/chiamata e parser pendenti.

## Fonti primarie

- https://www.ibm.com/docs/en/db2-for-zos/12.0.0?topic=procedures-sql-procedure-body

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.sql` | [hello.sql](variants/sql-614f3a43/hello.sql) creato, verifiche pendenti |
| `.db2` | [hello.db2](hello.db2) creato, verifiche pendenti |
