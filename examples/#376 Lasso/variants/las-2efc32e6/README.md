# 0376: Lasso: `.las`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#376 Lasso/hello.lasso9.

Required toolchain: Lasso9 originale; versione da registrare. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.las; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: stdout Hello, World! followed by newline.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.las`: `d14bbe0b20f4b5e8c8691bf03a8dadc548be880e3067d1bf83ae4f90f2c12764`

Primary sources:

- https://lassoguide.com/operations/command-line-tools.html
- https://lassoguide.com/language/variables.html
