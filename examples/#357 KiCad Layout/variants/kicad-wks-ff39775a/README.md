# 0357: KiCad Layout: `.kicad_wks`

Role: Drawing sheet KiCad with tbtext element of greeting; not PCB card.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Required genuine toolchain not available/configured, non disponibile / non verificata. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
KiCad Drawing Sheet Editor: aprire hello.kicad_wks
```

Expected result: Hello, World! in sheet

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.kicad_wks`: `a3a6e250bf2fccd2fb3bfc46564e7e4bfc5e9eed7122f40163e79b40673bf75f`

Primary sources:

- https://dev-docs.kicad.org/en/file-formats/sexpr-wks/
- https://docs.kicad.org/8.0/en/pl_editor/pl_editor.html
- https://dev-docs.kicad.org/en/file-formats/sexpr-pcb/
- https://docs.kicad.org/7.0/en/pcbnew/pcbnew.html
