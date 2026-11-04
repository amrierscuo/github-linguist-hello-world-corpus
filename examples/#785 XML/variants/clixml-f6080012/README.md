# 0785: XML: `.clixml`

Serialization CLIXML of a string; parser/import original still pendant.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.clixml`.

Control provided, from the folder of the variant:

```text
PowerShell Import-Clixml hello.clixml; assert returned string
```

Expected result: well-formed XML that preserves the greeting; application schema and import have not been verified.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.w3.org/TR/xml/](https://www.w3.org/TR/xml/)
- [https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/import-clixml](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/import-clixml)
