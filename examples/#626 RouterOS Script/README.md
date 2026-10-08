# #626 RouterOS Script

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Eseguire uno script RouterOS che stampa Hello, World!.

Script con variabile locale, concatenazione e :put; richiede un ambiente RouterOS di prova.

## Toolchain e riproduzione

RouterOS Script, versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
RouterOS: import hello.rsc
```

## Risultato atteso e stato

Hello, World! nella console RouterOS.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Runtime RouterOS non disponibile; esecuzione e parser pendenti.

## Fonti primarie

- https://help.mikrotik.com/docs/spaces/ROS/pages/47579229/Scripting

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.rsc` | [hello.rsc](hello.rsc) creato, verifiche pendenti |
