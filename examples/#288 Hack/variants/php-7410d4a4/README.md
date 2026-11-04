# 0288: Hack: `.php`

Role: Source Hack tagged <?hh and entry point HHVM; it is not a PHP program.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: HHVM/Hack e typechecker hh_client; versioni effettive da registrare. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
hh_client; hhvm hello.php
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.php`: `f0d3a9127b2b5314d4505c825137f6aa22e3e95e47aa32098a8d2af349498045`

Primary sources:

- https://docs.hhvm.com/hack/getting-started/getting-started
- https://docs.hhvm.com/hack/source-code-fundamentals/program-structure/
- https://hacklang.org/
