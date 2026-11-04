# #198 F#

Play a F# script and print Hello, World! followed by newline.

Canonical type `programming`, language_id `105`.

Suggested toolchain: F# Interactive (fsi), .NET SDK modern or FSharp.Compiler.Tools compatible.

From the example directory:

```sh
dotnet fsi --exec hello.fsx
```

Expected result: stdout `Hello, World!` followed by newline, 0. output

With FSI standalone for .NET Framework use fsi.exe --exec hello.fsx. The log indicates which of the two distributions has actually been tested.

Recorded status: syntax verified; behavior verified. Toolchain: FSharp.Compiler.Tools 10.2.3 — FSI standalone on .NET Framework. See [log](verification/verification.log).

Sources of linguaggio/formato and original implementations:

- [F# — riga di comando e FSI](https://learn.microsoft.com/en-us/dotnet/fsharp/get-started/get-started-command-line)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.fs` | [hello.fs](variants/ext-fs-2e6673/hello.fs) created; verification pending |
| `.fsi` | [Greeting.fsi](variants/ext-fsi-2e667369/Greeting.fsi) created; verification pending |
| `.fsx` | [hello.fsx](hello.fsx) verified |
