# 0408: MAXScript: `.mcr`

Role: MacroScript MAXScript recordable, print in Listener only on execute.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Autodesk 3ds Max MAXScript runtime. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
3ds Max: valutare hello.mcr; eseguire la macro CorpusGreeting in ambiente di test
```

Expected result: Hello, World! in Listener

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.mcr`: `65a32b61750d64c68133288fc281c3f15a852d8fc444334545b45abebeb3df04`

Primary sources:

- https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=GUID-6E21C768-7256-4500-AB1F-B144F492F055
- https://help.autodesk.com/view/MAXDEV/2026/ENU/
