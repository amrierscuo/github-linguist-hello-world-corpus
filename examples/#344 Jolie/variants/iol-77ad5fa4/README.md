# 0344: Jolie: `.iol`

Role: Jolie Interface includes: GreetingPort type and one-way statement; implementation in fixtures.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Required genuine toolchain not available/configured, non disponibile / non verificata. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Jolie: include hello.iol in progetto di test e compilare l’interfaccia; inviare greet con Hello, World! solo se host disponibile
```

Expected result: Accepted interface and given Greeting string

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.iol`: `1ed4d8c1416ca7dc3ee7d5f6768f912bfa55331199ff1973a4e74f6ac46f9816`

Primary sources:

- https://docs.jolie-lang.org/v1.13.x/language-tools-and-standard-library/basics/interfaces.html
- https://www.jolie-lang.org/
- https://docs.jolie-lang.org/v1.12.x/language-tools-and-standard-library/basics/fault-handling/scopes-and-faults/README.html
- https://github.com/jolie/jolie
