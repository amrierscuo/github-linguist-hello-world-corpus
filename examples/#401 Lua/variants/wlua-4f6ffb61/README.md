# 0401: Lua: `.wlua`

Role: Source Lua windowed for Windows host; same syntax Lua, stdout may not have a console.

Origin: Byte-identical copy of the original corpus source: examples/#401 Lua/hello.lua.

Required toolchain: Lua 5.4.8 native Linux build from original sources. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.wlua; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: The program requires a host with stdout or captured console to observe Hello, World!.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.wlua`: `07219cd9561b41ce1f39209958076c471b17855679c968b42767b0122423c782`

Primary sources:

- https://www.lua.org/manual/5.4/
