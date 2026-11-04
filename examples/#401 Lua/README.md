# #401 Lua

Stampare Hello, World! in Lua.

Canonical type `programming`, language_id `213`.

Suggested toolchain: Lua 5.4 original.

From the example directory:

```sh
lua hello.lua
```

Expected result: stdout Hello, World! and LF, 0. output

A standard Lua program without external libraries.

Recorded status: syntax verified; behavior verified. Toolchain: Lua 5.4.8 native Linux build from original sources. [Log](verification/result.json).

Sources:

- [Lua — manuale](https://www.lua.org/manual/5.4/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.lua` | [hello.lua](hello.lua), [corpus_hello.lua](variants/rockspec-6557708e/corpus_hello.lua) created; verification pending |
| `.fcgi` | [hello.fcgi](variants/fcgi-209194e4/hello.fcgi) created; verification pending |
| `.nse` | [hello.nse](variants/nse-0b7f3a91/hello.nse) created; verification pending |
| `.p8` | [hello.p8](variants/p8-3318ca99/hello.p8) created; verification pending |
| `.pd_lua` | [hello.pd_lua](variants/pd-lua-63a1006b/hello.pd_lua) created; verification pending |
| `.rbxs` | [hello.rbxs](variants/rbxs-06e5c9d4/hello.rbxs) created; verification pending |
| `.rockspec` | [corpus-hello-1.0-1.rockspec](variants/rockspec-6557708e/corpus-hello-1.0-1.rockspec) created; verification pending |
| `.wlua` | [hello.wlua](variants/wlua-4f6ffb61/hello.wlua) created; verification pending |
