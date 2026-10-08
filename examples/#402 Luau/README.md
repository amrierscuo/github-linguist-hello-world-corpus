# #402 Luau

Controllare i tipi Luau e stampare Hello, World! da una variabile string.

Tipo canonico `programming`, language_id `365050359`.

Toolchain prevista: Luau CLI e luau-analyze ufficiali.

Dalla cartella dell’esempio:

```sh
luau-analyze hello.luau
luau hello.luau
```

Risultato atteso: analisi senza errori; stdout Hello, World! e LF.

Luau è verificato col suo analizzatore/runtime, separatamente da Lua; non usa API Roblox.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Luau official release 0.741 Windows x64. [Log](verification/result.json). 

Fonti:

- [Luau — sintassi](https://luau.org/syntax)
- [Luau — release ufficiali](https://github.com/luau-lang/luau/releases)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.luau` | [hello.luau](hello.luau) verificato |
