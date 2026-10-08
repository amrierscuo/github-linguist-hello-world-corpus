# #084 C#

Stampare esattamente Hello, World! seguito da newline da un programma C# console.

## Toolchain

Microsoft C# compiler fatal error CS2007: Unrecognized option: '/version'; installed .NET Framework 4.x CLR on Windows

## Comandi e procedura

Da un prompt sviluppatore Windows in cui csc sia disponibile:

```powershell
New-Item -ItemType Directory -Force build
csc /nologo /version
csc /nologo /target:exe /out:build/Hello.exe Hello.cs
./build/Hello.exe
```

Nel test csc è stato invocato dal Framework64 di Windows e l'eseguibile
eseguito dal CLR .NET Framework installato. Il binario è conservato solo
nella cartella di lavoro, senza distribuirlo nel corpus.

## Risultato atteso

Compilazione exit 0; runtime exit 0, stdout Hello, World! più newline.

## Stato

Sintassi e semantica verificate.

Sorgente compatibile con il compilatore csc .NET Framework presente. Il log registra la versione del compilatore osservata; non è una prova di un diverso SDK .NET.

Verifica effettiva del 2026-10-08T11:33:09.613198+00:00 su Windows x64: [log](verification/result.json).
Il log include hash SHA-256 della sorgente e dei checker, versioni, comandi, codici di uscita, stdout, stderr e limiti della prova.

## Fonti primarie

- [https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/compiler-options/](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/compiler-options/)
- [https://learn.microsoft.com/en-us/dotnet/api/system.console.writeline](https://learn.microsoft.com/en-us/dotnet/api/system.console.writeline)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cs` | [Hello.cs](Hello.cs) verificato |
| `.cake` | [hello.cake](variants/ext-cake-2e63616b65/hello.cake) creato, verifiche pendenti |
| `.cs.pp` | [hello.cs.pp](variants/ext-cs-pp-2e63732e7070/hello.cs.pp) creato, verifiche pendenti |
| `.csx` | [hello.csx](variants/ext-csx-2e637378/hello.csx) creato, verifiche pendenti |
| `.linq` | [hello.linq](variants/ext-linq-2e6c696e71/hello.linq) creato, verifiche pendenti |
