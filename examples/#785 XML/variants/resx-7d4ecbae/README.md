# 0785: XML: `.resx`

Risorsa .NET RESX textuale, distinta da output binario .resources.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.resx`.

Control provided, from the folder of the variant:

```text
resgen hello.resx work/hello.resources or ResXResourceReader
```

Expected result: resource Greeting == Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.w3.org/TR/xml/](https://www.w3.org/TR/xml/)
- [https://learn.microsoft.com/en-us/dotnet/framework/resources/working-with-resx-files-programmatically](https://learn.microsoft.com/en-us/dotnet/framework/resources/working-with-resx-files-programmatically)
