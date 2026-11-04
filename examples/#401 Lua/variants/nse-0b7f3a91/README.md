# 0401: Lua: `.nse`

Role: Nmap NSE with prerule and greeting action; does not scan.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Lua 5.4.8 native Linux build from original sources. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
nmap --script-help hello.nse (offline, carica descriptor; action da verificare in harness originale senza target)
```

Expected result: NSE records the descriptor; action returns Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.nse`: `ca521774b0b7c7a373901a1487b54c48f3170d491bc793e48427094f182b87a6`

Primary sources:

- https://nmap.org/book/nse-script-format.html
- https://www.lua.org/manual/5.4/
