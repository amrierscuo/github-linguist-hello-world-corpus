# 0401: Lua: `.rockspec`

Role: Descriptor LuaRocks: Lua data with summary and module mapping, no print program.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Lua 5.4.8 native Linux build from original sources. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
luarocks lint corpus-hello-1.0-1.rockspec; in build locale generare il tar del fixture e luarocks make
```

Expected result: Descriptor registered; module returns Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `corpus-hello-1.0-1.rockspec`: `04b95ae9c6ce6c4f2b19987c53644f86e093fb1d94304b2a83c5ff9071f877c1`
- `corpus_hello.lua`: `c6472388da8d915a57c4073b4fd9cabdbf9a3ec35a84fe263cf6b4b839aa7c23`

Primary sources:

- https://github.com/luarocks/luarocks/blob/main/docs/rockspec_format.md
- https://www.lua.org/manual/5.4/
