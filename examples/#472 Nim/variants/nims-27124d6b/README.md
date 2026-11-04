# 0472: Nim: `.nims`

Ruolo: NimScript con istruzione top-level echo, separato da codice C generato Nim.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Nim1.6.14 Ubuntu, backend C/GCC. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
nim e hello.nims
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.nims`: `cf4de8709c40d3e7cc30fb5e859b52358f9f0f6c9241551d49f3c09c4ce5bdb6`

Primary sources:

- https://nim-lang.org/docs/nims.html
- https://nim-lang.org/docs/tut1.html
