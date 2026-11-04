# 0463: Nearley: `.nearley`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#463 Nearley/hello.ne.

Required toolchain: Nearley2.20.1, Node22.20.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
nearleyc hello.nearley -o hello.js; node verify.js
```

Expected result: Hello, World! followed by newline; exit0.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.nearley`: `3a88908ad98babe930774529f396d9e79b5d6e41f37dc2ad6f91f13d6851901a`
- `verify.js`: `7093458dba252c87d7ac4fe1360c804159d75dc3b076db78243a006561819fc7`

Primary sources:

- https://nearley.js.org/docs/grammar
- https://nearley.js.org/docs/parser
