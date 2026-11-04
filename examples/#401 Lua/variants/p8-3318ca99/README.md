# 0401: Lua: `.p8`

Role: Cartridge PICO - 8 text with header/version and section __lua_; greeting is drawn in _draw.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Lua 5.4.8 native Linux build from original sources. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
PICO-8: load hello.p8; run
```

Expected result: Hello, World! screen

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.p8`: `69b1187af68e835a7a5f603b681ff580c07aa1ba9f81af74401b930dd71f3952`

Primary sources:

- https://www.lexaloffle.com/dl/docs/pico-8_manual.html
- https://www.lua.org/manual/5.4/
