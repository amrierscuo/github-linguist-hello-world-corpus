# #710 Tcsh

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Eseguire Tcsh e stampare Hello, World!.

Lo script usa set ed espansione della variabile; -f disabilita i file di avvio personali.

## Toolchain e riproduzione

Tcsh6.24.10 originale

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
tcsh -f hello.tcsh
```

## Risultato atteso e stato

Hello, World! su stdout.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://www.tcsh.org/

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.tcsh` | [hello.tcsh](hello.tcsh) verificato |
| `.csh` | [hello.csh](variants/csh-6f61e238/hello.csh) creato, verifiche pendenti |
