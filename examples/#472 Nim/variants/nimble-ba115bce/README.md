# 0472: Nim: `.nimble`

Ruolo: Manifest Nimble in NimScript con metadata e task hello.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Nim1.6.14 Ubuntu, backend C/GCC. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
nimble hello
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.nimble`: `c9cbdcadd41ecac468bfc3894695dc1d6233a260b57cb2183cc9452da33961de`

Primary sources:

- https://github.com/nim-lang/nimble#creating-packages
- https://nim-lang.org/docs/tut1.html
