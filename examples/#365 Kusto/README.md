# #365 Kusto

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Analizzare Kusto e restituire, con il motore query, la colonna greeting contenente Hello, World!.

Il driver carica l’assembly originale Microsoft, usa ParseAndAnalyze e confronta le diagnostiche. print e strcat sono operatori/funzioni Kusto; la verifica del parser non esegue una query sul servizio.

## Toolchain e riproduzione

Microsoft.Azure.Kusto.Language12.4.1; PowerShell7 per il driver; query engine non preparato

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
pwsh -NoProfile -File verify.ps1 /path/to/Kusto.Language.dll
```

## Risultato atteso e stato

Parser e analizzatore producono zero diagnostiche; engine atteso: una riga greeting=Hello, World!.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: no.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

Impedimenti: Motore Kusto non disponibile; esecuzione della query pendente.

## Fonti primarie

- https://learn.microsoft.com/en-us/kusto/query/print-operator
- https://learn.microsoft.com/en-us/kusto/query/strcat-function
- https://github.com/microsoft/Kusto-Query-Language

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.csl` | [hello.csl](variants/csl-341667e5/hello.csl) creato, verifiche pendenti |
| `.kql` | [hello.kql](hello.kql) sintassi verificata |
