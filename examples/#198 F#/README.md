# #198 F#

Interpretare uno script F# e stampare Hello, World! seguito da newline.

Tipo canonico `programming`, language_id `105`.

Toolchain prevista: F# Interactive (fsi), .NET SDK moderno oppure FSharp.Compiler.Tools compatibile.

Dalla cartella dell’esempio:

```sh
dotnet fsi --exec hello.fsx
```

Risultato atteso: stdout `Hello, World!` seguito da newline, uscita 0.

Con FSI standalone per .NET Framework usare fsi.exe --exec hello.fsx. Il log indica quale delle due distribuzioni è stata effettivamente provata.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: FSharp.Compiler.Tools 10.2.3 — FSI standalone on .NET Framework. Vedere [log](verification/verification.log). 

Fonti del linguaggio/formato e implementazioni originali:

- [F# — riga di comando e FSI](https://learn.microsoft.com/en-us/dotnet/fsharp/get-started/get-started-command-line)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.fs` | [hello.fs](variants/ext-fs-2e6673/hello.fs) creato, verifiche pendenti |
| `.fsi` | [Greeting.fsi](variants/ext-fsi-2e667369/Greeting.fsi) creato, verifiche pendenti |
| `.fsx` | [hello.fsx](hello.fsx) verificato |
