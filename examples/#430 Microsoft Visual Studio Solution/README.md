# #430 Microsoft Visual Studio Solution

Interpret a Visual Studio solution with MSBuild and fill out the referencing console project.

Canonical type `data`, language_id `849523096`.

Suggested toolchain: MSBuild .NET Framework 4.x and C# compiler.

From the example directory:

```sh
MSBuild.exe Hello.sln /t:Build /p:Configuration=Debug
build/Hello.exe
```

Expected result: solution build successful; stdout Hello, World! and newline.

The format is a minimal solution compatible with MSBuild legacy. The GUID are original fixture identifiers.

Recorded status: syntax verified; behavior verified. Toolchain: MSBuild .NET Framework 4.8 native compiler. [Log](verification/result.json).

Sources:

- [Microsoft — file solution .sln](https://learn.microsoft.com/en-us/visualstudio/extensibility/internals/solution-dot-sln-file)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.sln` | [Hello.sln](Hello.sln) verified |
