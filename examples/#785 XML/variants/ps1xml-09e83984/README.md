# 0785: XML: `.ps1xml`

PowerShell formatting date for strings; companion produces greeting.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.ps1xml`.

Control provided, from the folder of the variant:

```text
PowerShell isolated process: Update-FormatData -PrependPath hello.ps1xml; run greet.ps1
```

Expected result: well-formed XML that preserves the greeting; application schema and import have not been verified.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.w3.org/TR/xml/](https://www.w3.org/TR/xml/)
- [https://learn.microsoft.com/en-us/powershell/scripting/developer/format/formatting-file-overview](https://learn.microsoft.com/en-us/powershell/scripting/developer/format/formatting-file-overview)
