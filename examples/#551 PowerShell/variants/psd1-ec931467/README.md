# 0551: PowerShell: `.psd1`

Role: Manifest PowerShell module, hashtable of only data; RootModule is a separate fixture.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: PowerShell7.6.5 originale Windows. The log records the version used for the check. Other application environments remain unverified.

Proposed verification procedure, not performed, by the directory of the variant:

```text
pwsh -NoProfile -Command "Test-ModuleManifest ./hello.psd1; Import-Module ./hello.psd1; Get-CorpusGreeting"
```

Expected result: Accepted Manifest and Hello, World! from function

Individual status: artifact created `true`, syntax verified `true`, behavior verified `true`. Greeting data or configuration alone does not establish execution.

Blockers:

- No impediment for the scope actually verified.

SHA-256 of variant files:

- `hello.psd1`: `c50399a95f7107c81eeeb8071bb1b890cf137543a25d09ccd07be62485824392`
- `hello.psm1`: `d22db22d41450b8c24a67bf19c2a5ff3b163c928d1344b899852a99f4ac0ca78`

Primary sources:

- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_module_manifests
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-output

Additive test actually performed:

Original PowerShell: module import; for .psd1 Test-ModuleManifest; exported function performed and exact stdout.

Log: `verification/native.json`. The proposed procedures above that were not run are distinct from the commands recorded in the log.

Tool/versione osservata: 7.6.5
