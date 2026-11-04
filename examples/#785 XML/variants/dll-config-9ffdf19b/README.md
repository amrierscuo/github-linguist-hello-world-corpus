# 0785: XML: `.dll.config`

Config .NET di libreria/app con appSettings; nessun assembly fittizio.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.dll.config`.

Control provided, from the folder of the variant:

```text
System.Configuration mapped configuration read, isolated file
```

Expected result: well-formed XML that preserves the greeting; application schema and import have not been verified.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.w3.org/TR/xml/](https://www.w3.org/TR/xml/)
- [https://learn.microsoft.com/en-us/dotnet/framework/configure-apps/file-schema/](https://learn.microsoft.com/en-us/dotnet/framework/configure-apps/file-schema/)
