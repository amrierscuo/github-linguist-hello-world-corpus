# 0065 Bicep: variant `.bicepparam`

Role: Bicep parameter files, associated with a module with declared parameter.

Type: **adapted**. Starting model: examples/#065 Bicep/hello.bicep; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
bicep build-params hello.bicepparam --outfile <output>/parameters.json; bicep build main.bicep --outfile <output>/template.json
```

Expected result: Hello, World!

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://learn.microsoft.com/azure/azure-resource-manager/bicep/outputs](https://learn.microsoft.com/azure/azure-resource-manager/bicep/outputs)
- [https://github.com/Azure/bicep/releases](https://github.com/Azure/bicep/releases)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/parameter-files](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/parameter-files)
