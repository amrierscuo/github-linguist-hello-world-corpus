# 0288: Hack: `.hhi`

Role: Hack HHI interface with statement only; implementation is in .hack. fixtures

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: HHVM/Hack e typechecker hh_client; versioni effettive da registrare. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
hh_client in progetto che espone hello.hhi e la relativa implementazione; hhvm driver.hack
```

Expected result: Greeting statement(): string; Hello, World! print driver

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.
- HHI and implementation must be configured as an external library interface, avoiding duplicate statements in the same project.

SHA-256 of variant files:

- `driver.hack`: `f0d3a9127b2b5314d4505c825137f6aa22e3e95e47aa32098a8d2af349498045`
- `hello.hhi`: `3bfa59fd2f621765b13cc70311275bf02f3dbdb63efb3fd22fb3f7309b195ce9`

Primary sources:

- https://docs.hhvm.com/hack/getting-started/getting-started
- https://docs.hhvm.com/hack/source-code-fundamentals/program-structure/
- https://hacklang.org/
