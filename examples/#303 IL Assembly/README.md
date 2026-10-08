# #303 IL Assembly

Assemblare CIL .NET e invocare Console.WriteLine da Main.

## Toolchain

Microsoft .NET Framework IL Assembler 4.8.9221.0 / CLR v4

## Comandi e procedura

ilasm /exe /output:build/Hello.exe hello.il; build/Hello.exe

## Risultato atteso

Assemblaggio e runtime exit 0; Hello, World! più newline.

## Stato

Sintassi e semantica verificate.

Questa voce è IL Assembly per CLR. .entrypoint, ldstr, call e ret sono assemblati dal tool originale. L’eseguibile compilato resta in work.

Verifica effettiva del 2026-10-08T12:29:57.289941+00:00 su Windows x64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://learn.microsoft.com/en-us/dotnet/framework/tools/ilasm-exe-il-assembler](https://learn.microsoft.com/en-us/dotnet/framework/tools/ilasm-exe-il-assembler)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.il` | [hello.il](hello.il) verificato |
