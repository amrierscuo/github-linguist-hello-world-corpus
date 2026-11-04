# 0401: Lua: `.rbxs`

Role: Textual Script Roblox Luau with print; not a Roblox binary model.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Lua 5.4.8 native Linux build from original sources. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Roblox Studio: importare il testo come Script e leggere Output in progetto locale
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.rbxs`: `07219cd9561b41ce1f39209958076c471b17855679c968b42767b0122423c782`

Primary sources:

- https://create.roblox.com/docs/luau
- https://www.lua.org/manual/5.4/
