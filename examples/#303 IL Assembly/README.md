# #303 IL Assembly

Assemblare CIL .NET e invocare Console.WriteLine da Main.

## Toolchain

Microsoft .NET Framework IL Assembler 4.8.9221.0 / CLR v4

## Commands and procedure

ilasm /exe /output: build/Hello.exe hello.il; build/Hello.exe

## Expected result

Assembly and runtime exit 0; Hello, World! plus newline.

## Status

syntax and behavior verified.

This entry is IL Assembly for CLR. .entrypoint, ldstr, call and ret are assembled by the original tool.

Actual verification of 2026-10-08T12:29:57.289941+00:00 on Windows x64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://learn.microsoft.com/en-us/dotnet/framework/tools/ilasm-exe-il-assembler](https://learn.microsoft.com/en-us/dotnet/framework/tools/ilasm-exe-il-assembler)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.il` | [hello.il](hello.il) verified |
