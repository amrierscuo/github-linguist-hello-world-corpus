# #402 Luau

Check Luau types and print Hello, World! from a string variable.

Canonical type `programming`, language_id `365050359`.

Suggested toolchain: Luau CLI and official luau-analyze.

From the example directory:

```sh
luau-analyze hello.luau
luau hello.luau
```

Risultato atteso: analisi senza errori; stdout Hello, World! e LF.

Luau is verified with its analizzatore/runtime, separately from Lua; it does not use API Roblox.

Recorded status: syntax verified; behavior verified. Toolchain: Luau official release 0.741 Windows x64. [Log](verification/result.json).

Sources:

- [Luau — sintassi](https://luau.org/syntax)
- [Luau — release ufficiali](https://github.com/luau-lang/luau/releases)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.luau` | [hello.luau](hello.luau) verified |
