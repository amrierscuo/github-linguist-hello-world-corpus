# #401 Lua

Stampare Hello, World! in Lua.

Tipo canonico `programming`, language_id `213`.

Toolchain prevista: Lua 5.4 originale.

Dalla cartella dell’esempio:

```sh
lua hello.lua
```

Risultato atteso: stdout Hello, World! e LF, uscita 0.

Un programma Lua standard senza librerie esterne.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Lua 5.4.8 native Linux build from original sources. [Log](verification/result.json). 

Fonti:

- [Lua — manuale](https://www.lua.org/manual/5.4/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.lua` | [hello.lua](hello.lua), [corpus_hello.lua](variants/rockspec-6557708e/corpus_hello.lua) creato, verifiche pendenti |
| `.fcgi` | [hello.fcgi](variants/fcgi-209194e4/hello.fcgi) creato, verifiche pendenti |
| `.nse` | [hello.nse](variants/nse-0b7f3a91/hello.nse) creato, verifiche pendenti |
| `.p8` | [hello.p8](variants/p8-3318ca99/hello.p8) creato, verifiche pendenti |
| `.pd_lua` | [hello.pd_lua](variants/pd-lua-63a1006b/hello.pd_lua) creato, verifiche pendenti |
| `.rbxs` | [hello.rbxs](variants/rbxs-06e5c9d4/hello.rbxs) creato, verifiche pendenti |
| `.rockspec` | [corpus-hello-1.0-1.rockspec](variants/rockspec-6557708e/corpus-hello-1.0-1.rockspec) creato, verifiche pendenti |
| `.wlua` | [hello.wlua](variants/wlua-4f6ffb61/hello.wlua) creato, verifiche pendenti |
