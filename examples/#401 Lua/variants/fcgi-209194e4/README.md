# 0401: Lua: `.fcgi`

Role: Script Lua FastCGI for binding Lua MSYS documented: a request on socket FD 0 inherited, response and finish.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Lua 5.4.8 native Linux build from original sources. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Host Lua MSYS FastCGI: socket FD 0 ereditato da un processo di test; una sola richiesta di test e cleanup
```

Expected result: FastCGI response with Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.
- Binding fcgi Lua MSYS unprepared; no socket is created in this preparation.

SHA-256 of variant files:

- `hello.fcgi`: `c819d3acb5b468c607b1a0c1e3dbbd7dff54df2d028e54cf1720554f5bdb20ba`

Primary sources:

- https://lua.msys.ch/lua-module-reference.html
- https://www.lua.org/manual/5.4/
