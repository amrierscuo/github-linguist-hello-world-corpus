# 0530: Pawn: `.sma`

Role: Plugin AMX Mod X Pawn: includes amxmodx and callback plugin_init, not main console.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Required genuine compiler/runtime, non disponibile / non verificata. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
AMX Mod X compiler: amxxpc hello.sma; caricare solo in server di test locale
```

Expected result: Hello, World! in the log server

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.sma`: `838dc2e7cd55213665d125ecbc0f9af8d2d0892d576a57651c53db6f8d405016`

Primary sources:

- https://www.amxmodx.org/doc/
- https://compuphase.com/pawn/pawn.htm
