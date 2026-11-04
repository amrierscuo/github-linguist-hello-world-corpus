# 0551: PowerShell: `.psm1`

Ruolo: Modulo PowerShell con funzione pubblica; Export-ModuleMember evita main top-level.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: PowerShell7.6.5 originale Windows. The log records the version used for the check. Other application environments remain unverified.

Proposed verification procedure, not performed, by the directory of the variant:

```text
pwsh -NoProfile -Command "Import-Module ./hello.psm1; Get-CorpusGreeting"
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `true`, behavior verified `true`. Greeting data or configuration alone does not establish execution.

Blockers:

- No impediment for the scope actually verified.

SHA-256 of variant files:

- `hello.psm1`: `363ba5e1c6cbede4bcf7e700f92b7472b39c4b13e632d88bd020a2b76a57c78e`

Primary sources:

- https://learn.microsoft.com/en-us/powershell/scripting/developer/module/how-to-write-a-powershell-script-module
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-output

Additive test actually performed:

Original PowerShell: module import; for .psd1 Test-ModuleManifest; exported function performed and exact stdout.

Log: `verification/native.json`. The proposed procedures above that were not run are distinct from the commands recorded in the log.

Tool/versione osservata: 7.6.5
