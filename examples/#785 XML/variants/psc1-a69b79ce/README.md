# 0785: XML: `.psc1`

PowerShell console descriptor without snap-in; companion performs greeting in the trial process.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.psc1`.

Control provided, from the folder of the variant:

```text
powershell.exe -NoProfile -PSConsoleFile hello.psc1 -File greet.ps1
```

Expected result: well-formed XML that preserves the greeting; application schema and import have not been verified.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.w3.org/TR/xml/](https://www.w3.org/TR/xml/)
- [https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/export-console](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/export-console)
