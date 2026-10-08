# #430 Microsoft Visual Studio Solution

Interpretare una solution Visual Studio con MSBuild e compilare il progetto console referenziato.

Tipo canonico `data`, language_id `849523096`.

Toolchain prevista: MSBuild .NET Framework 4.x e C# compiler.

Dalla cartella dell’esempio:

```sh
MSBuild.exe Hello.sln /t:Build /p:Configuration=Debug
build/Hello.exe
```

Risultato atteso: solution build riuscita; stdout Hello, World! e newline.

Il formato è una solution minimale compatibile con MSBuild legacy. I GUID sono identificatori originali del fixture.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: MSBuild .NET Framework 4.8 native compiler. [Log](verification/result.json). 

Fonti:

- [Microsoft — file solution .sln](https://learn.microsoft.com/en-us/visualstudio/extensibility/internals/solution-dot-sln-file)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.sln` | [Hello.sln](Hello.sln) verificato |
