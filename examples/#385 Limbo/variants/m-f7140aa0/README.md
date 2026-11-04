# 0385: Limbo: `.m`

Ruolo: Interfaccia di modulo Limbo: dichiarazioni pubbliche, nessun implement init.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Inferno/Limbo; versione da registrare. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Limbo: includere draw.m e hello.m nel modulo hello.b, compilare con limbo e invocare init
```

Expected result: Accepted Hello module interface; Hello, World! print implementation

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.
- The original fixture already states Hello inline: replace that statement with includes "hello.m" in the build directory, keeping the main source intact.

SHA-256 of variant files:

- `hello.b`: `aad0676a4f4d15fc631c51c3543141e77763337b62eebf8763392a9650791c28`
- `hello.m`: `b7645ca6b02dd10fefd462bdaacf2cd1836c87189f8b510acb5425fbffb234d0`

Primary sources:

- https://inferno-os.org/inferno/limbo.html
- https://www.vitanuova.com/inferno/limbo.html
- https://www.vitanuova.com/inferno/papers/limbo.html
