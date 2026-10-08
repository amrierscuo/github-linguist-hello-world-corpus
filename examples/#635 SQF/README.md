# #635 SQF

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Eseguire SQF e scrivere Hello, World! nel log.

La variabile locale viene formattata da format e scritta con diag_log; un generico parser C non sostituisce SQF.

## Toolchain e riproduzione

VM SQF Arma, versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
Arma: [] execVM "hello.sqf"
```

## Risultato atteso e stato

Hello, World! nel log SQF.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Runtime SQF/Arma non disponibile; verifiche pendenti.

## Fonti primarie

- https://community.bohemia.net/wiki/diag_log

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.sqf` | [hello.sqf](hello.sqf), [main.sqf](variants/hqf-981d9d8f/main.sqf) creato, verifiche pendenti |
| `.hqf` | [hello.hqf](variants/hqf-981d9d8f/hello.hqf) creato, verifiche pendenti |
