# 0084 C#: variant `.linq`

Ruolo: Query LINQPad di tipo Program, con header XML LINQPad e Main.

Type: **adapted**. Starting model: examples/#084 C#/Hello.cs; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
LINQPad/lprun: aprire ed eseguire hello.linq come Program.
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

- [https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/compiler-options/](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/compiler-options/)
- [https://learn.microsoft.com/en-us/dotnet/api/system.console.writeline](https://learn.microsoft.com/en-us/dotnet/api/system.console.writeline)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://www.linqpad.net/](https://www.linqpad.net/)
