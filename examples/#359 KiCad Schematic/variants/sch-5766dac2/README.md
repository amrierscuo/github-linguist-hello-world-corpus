# 0359: KiCad Schematic: `.sch`

Role: Schematic KiCad legacy v4 text with Text Notes, distinct from the modern s-expression.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Required genuine toolchain not available/configured, non disponibile / non verificata. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
KiCad: aprire hello.sch e controllare il testo prima dell’eventuale conversione
```

Expected result: Note Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.sch`: `0393945aa8d920e64448988c3c5bb6a4359ebab47f0d5f218be524f76ab78cd5`

Primary sources:

- https://dev-docs.kicad.org/en/file-formats/legacy-4-to-6/legacy_file_format_documentation.pdf
- https://dev-docs.kicad.org/en/file-formats/sexpr-schematic/
- https://docs.kicad.org/7.0/en/eeschema/eeschema.html
