# #432 MiniScript

Stampare Hello, World! in MiniScript.

Tipo canonico `programming`, language_id `704299647`.

Toolchain prevista: MiniScript CLI originale.

Dalla cartella dell’esempio:

```sh
csc /nologo /out:build/verify.exe Verify.cs <percorsi MiniScript-cs/Miniscript*.cs>
build/verify.exe
```

Risultato atteso: stdout Hello, World! e newline.

Non è MAXScript: stessa estensione, linguaggio e runtime distinti.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Original JoeStrout MiniScript C# sources at b4510312059df4288af3ce849b235535a4e1bfa7 + Microsoft Roslyn Toolset 4.8.0 / .NET Framework. [Log](verification/result.json). 

Fonti:

- [MiniScript — print](https://miniscript.org/wiki/Print)
- [MiniScript — sorgenti ufficiali](https://github.com/JoeStrout/miniscript)

Il checker usa la implementazione C# originale di JoeStrout/miniscript al commit `b4510312059df4288af3ce849b235535a4e1bfa7`, scaricando senza modifiche i sorgenti MiniScript-cs/Miniscript*.cs. Interpreter.Compile e RunUntilDone analizzano/eseguono hello.ms; errori del motore causano fallimento.

Il checker usa la implementazione C# originale di JoeStrout/miniscript al commit `b4510312059df4288af3ce849b235535a4e1bfa7`, scaricando senza modifiche i sorgenti MiniScript-cs/Miniscript*.cs. Interpreter.Compile e RunUntilDone analizzano/eseguono hello.ms; errori del motore causano fallimento.

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ms` | [hello.ms](hello.ms) verificato |
