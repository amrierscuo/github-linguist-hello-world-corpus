# 0376: Lasso: `.lasso8`

Role: Template Lasso 8 bracket syntax with string expression; distinct from the template Lasso 9.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Lasso9 originale; versione da registrare. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Lasso 8: servire il template hello.lasso8 da host di test
```

Expected result: Hello, World! in rendering

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.lasso8`: `0431588ad84fbfc41ca0c7e1341ab5d0586ec5a47237fc88be6b8f095c75821a`

Primary sources:

- https://www.lassosoft.com/Lasso-8-Documentation
- https://lassoguide.com/operations/command-line-tools.html
- https://lassoguide.com/language/variables.html
