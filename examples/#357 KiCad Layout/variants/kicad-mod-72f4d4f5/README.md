# 0357: KiCad Layout: `.kicad_mod`

Role: Footprint of library with fp_text user of greeting, distinguished by PCB card.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Required genuine toolchain not available/configured, non disponibile / non verificata. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
KiCad Footprint Editor: importare hello.kicad_mod e visualizzare il testo
```

Expected result: Hello, World! on the silkscreen of the footprint

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.kicad_mod`: `9b2cc5fd1f5cf072bb7cf5e956c162b79e6237ed9918294560872e982b438a74`

Primary sources:

- https://dev-docs.kicad.org/en/file-formats/sexpr-footprint/
- https://dev-docs.kicad.org/en/file-formats/sexpr-pcb/
- https://docs.kicad.org/7.0/en/pcbnew/pcbnew.html
