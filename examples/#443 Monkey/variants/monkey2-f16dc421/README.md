# 0443: Monkey: `.monkey2`

Role: Monkey2 program with import std and namespace, distinct from the syntax Monkey X.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Required genuine toolchain not available/configured, non disponibile / non verificata. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Monkey2 mx2cc: compilare hello.monkey2 e avviare programma locale
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.monkey2`: `a4d68b1bdf3594af5db37931800ab99c7afaf406775fcce0046cd861fc05b344`

Primary sources:

- https://github.com/blitz-research/monkey2
- https://github.com/blitz-research/monkey
