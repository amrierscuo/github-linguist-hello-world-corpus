# 0401: Lua: `.pd_lua`

Role: Class Pd-Lua pdlua with bang method and symbolic outlet, do not print Lua standalone.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Lua 5.4.8 native Linux build from original sources. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Pure Data con pdlua: creare [hello], inviare bang e leggere outlet con [print]
```

Expected result: Simbolo Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.pd_lua`: `1889785b2e68c5d26445d1a5fd3b7790a8999a87be2124fb91b245677a8af75f`

Primary sources:

- https://github.com/agraef/pd-lua
- https://www.lua.org/manual/5.4/
