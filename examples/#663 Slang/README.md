# #663 Slang

Compilare un compute shader Slang che scrive i codici ASCII del saluto.

Tipo canonico `programming`, language_id `239357863`.

Toolchain prevista: Slang v2026.19 official Windows compiler; SPIR-V compile verified, GPU execution pending.

Dalla cartella dell’esempio:

```sh
slangc hello.slang -entry main -target spirv -o build/hello.spv
```

Risultato atteso: shader compilato; dispatch restituisce ASCII Hello, World!.

Slang è il linguaggio shader del compiler shader-slang; la semantica GPU non deriva dal solo output SPIR-V.

Stato registrato: sintassi verificata; semantica in attesa. Toolchain: Slang official Windows release v2026.19. [Log](verification/result.json). Compiler Slang genera SPIR-V; host GPU e dispatch non eseguiti.

Fonti:

- [Shader Slang](https://shader-slang.org/docs/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.slang` | [hello.slang](hello.slang) sintassi verificata |
