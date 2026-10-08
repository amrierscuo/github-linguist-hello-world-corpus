# #551 PowerShell

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Eseguire PowerShell e stampare Hello, World!.

Il programma concatena audience e usa Write-Output. Il profilo personale non viene caricato.

## Toolchain e riproduzione

PowerShell7.6.5 originale Windows

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
pwsh -NoProfile -File hello.ps1
```

## Risultato atteso e stato

Hello, World! seguito da newline; exit0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-output

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ps1` | [hello.ps1](hello.ps1) verificato |
| `.psd1` | [hello.psd1](variants/psd1-ec931467/hello.psd1) verificato |
| `.psm1` | [hello.psm1](variants/psm1-51d244a0/hello.psm1) verificato |
