# 0785: XML: `.slnx`

Fixture Visual Studio solution XML con folder originale; nessun progetto esterno.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.slnx`.

Control provided, from the folder of the variant:

```text
dotnet sln hello.slnx list in an isolated folder
```

Expected result: well-formed XML that preserves the greeting; application schema and import have not been verified.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.w3.org/TR/xml/](https://www.w3.org/TR/xml/)
- [https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-sln](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-sln)
