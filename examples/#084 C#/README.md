# #084 C#

Print exactly Hello, World! followed by newline from a C# console program.

## Toolchain

Microsoft C# compiler fatal error CS2007: Unrecognized option: '/version'; installed .NET Framework 4.x CLR on Windows

## Commands and procedure

From a Windows developer prompt where csc is available:

```powershell
New-Item -ItemType Directory -Force build
csc /nologo /version
csc /nologo /target:exe /out:build/Hello.exe Hello.cs
./build/Hello.exe
```

In the csc test it was invoked by the Windows Framework64 and the executable
executed by the CLR .NET Framework installed.
in the workbook, without distributing it in the corpus.

## Expected result

Exit 0; runtime exit 0, stdout Hello, World! plus newline.

## Status

syntax and behavior verified.

Source compatible with the csc .NET Framework compiler present. The log records the version of the observed compiler; it is not a proof of a different SDK .NET.

Actual verification of 2026-10-08T11:33:09.613198+00:00 on Windows x64: [log](verification/result.json).
The log includes hash SHA-256 of the source and the checkers, versions, commands, exit codes, stdout, stderr and test limits.

## Primary sources

- [https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/compiler-options/](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/compiler-options/)
- [https://learn.microsoft.com/en-us/dotnet/api/system.console.writeline](https://learn.microsoft.com/en-us/dotnet/api/system.console.writeline)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cs` | [Hello.cs](Hello.cs) verified |
| `.cake` | [hello.cake](variants/ext-cake-2e63616b65/hello.cake) created; verification pending |
| `.cs.pp` | [hello.cs.pp](variants/ext-cs-pp-2e63732e7070/hello.cs.pp) created; verification pending |
| `.csx` | [hello.csx](variants/ext-csx-2e637378/hello.csx) created; verification pending |
| `.linq` | [hello.linq](variants/ext-linq-2e6c696e71/hello.linq) created; verification pending |
