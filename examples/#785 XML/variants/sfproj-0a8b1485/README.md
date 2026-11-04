# 0785: XML: `.sfproj`

Fixture MSBuild XML with PropertyGroup and Target; .sfproj extension retains the role of project/import/profile. Does not declare SDK/deployment/compiler configured vendor.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.sfproj`.

Control provided, from the folder of the variant:

```text
MSBuild hello.sfproj /t:Greeting (process/project isolato)
```

Expected result: well-formed XML that preserves the greeting; application schema and import have not been verified.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.w3.org/TR/xml/](https://www.w3.org/TR/xml/)
- [https://learn.microsoft.com/en-us/visualstudio/msbuild/msbuild-project-file-schema-reference](https://learn.microsoft.com/en-us/visualstudio/msbuild/msbuild-project-file-schema-reference)
