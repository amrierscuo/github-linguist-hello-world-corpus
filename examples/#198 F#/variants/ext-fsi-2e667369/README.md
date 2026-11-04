# 0198 F#: variant `.fsi`

Role: Signature F# fsi, which binds the implementation unit of the same name.

Type: **adapted**. Starting model: examples/#198 F#/hello.fsx; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
F# compiler: compilare Greeting.fsi, Greeting.fs, Program.fs in questo ordine nel progetto esterno; eseguire.
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

- [https://learn.microsoft.com/en-us/dotnet/fsharp/get-started/get-started-command-line](https://learn.microsoft.com/en-us/dotnet/fsharp/get-started/get-started-command-line)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://learn.microsoft.com/en-us/dotnet/fsharp/language-reference/signature-files](https://learn.microsoft.com/en-us/dotnet/fsharp/language-reference/signature-files)
