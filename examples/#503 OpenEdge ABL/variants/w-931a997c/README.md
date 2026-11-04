# 0503: OpenEdge ABL: `.w`

Role: Window procedures ABL: creates a local widget window with greeting title, destroyed at the end of the test.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Progress OpenEdge ABL. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
OpenEdge GUI: RUN hello.w in sessione locale di test; chiudere la finestra
```

Expected result: Window with title Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.w`: `d6dcfdd375626f4cf5acd83d58df8e33acd149000bd6a11f271142f8d3d0f2ca`

Primary sources:

- https://documentation.progress.com/output/ua/OpenEdge_latest/gsins/openedge-file-types.html
- https://docs.progress.com/bundle/abl-reference/page/MESSAGE-statement.html
