# 0359: KiCad Schematic: `.kicad_sym`

Role: Bookcase KiCad symbols with Value property of greeting, distinct from schematic.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Required genuine toolchain not available/configured, non disponibile / non verificata. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
KiCad Symbol Editor: aprire/importare hello.kicad_sym
```

Expected result: Greeting Symbol with Value Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.kicad_sym`: `282187cb51a3956825f982795eadf5d64e709c8945ec917088986323ed03e992`

Primary sources:

- https://dev-docs.kicad.org/en/file-formats/sexpr-symbol-lib/
- https://dev-docs.kicad.org/en/file-formats/sexpr-schematic/
- https://docs.kicad.org/7.0/en/eeschema/eeschema.html
