# #551 PowerShell

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Eseguire PowerShell e stampare Hello, World!.

Il programma concatena audience e usa Write-Output. Il profilo personale non viene caricato.

## Toolchain and reproduction

PowerShell7.6.5 originale Windows

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
pwsh -NoProfile -File hello.ps1
```

## Expected result and status

Hello, World! seguito da newline; exit0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-output

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ps1` | [hello.ps1](hello.ps1) verified |
| `.psd1` | [hello.psd1](variants/psd1-ec931467/hello.psd1) verified |
| `.psm1` | [hello.psm1](variants/psm1-51d244a0/hello.psm1) verified |
