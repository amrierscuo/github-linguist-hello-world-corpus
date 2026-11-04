# 0533: Pic: `.chem`

Role: DSL chem for benzene ring and documented Pic insert of a label; distinct from the Pic .PS. block

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Genuine GNU Pic and groff ASCII renderer, GNU pic (groff) version 1.23.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
chem hello.chem | groff -p -Tps > hello.ps
```

Expected result: Chemical Diagram labeled Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.
- The chem/pic combination must still be interpreted by the original tool; no verification is inherited by Pic.

SHA-256 of variant files:

- `hello.chem`: `808dc33a8c6f4659d1393b523fef3f8764a3b23fc5edc1551e3ae3a411b60c9b`

Primary sources:

- https://www.gnu.org/software/groff/manual/groff-man-pages.pdf
- https://www.gnu.org/software/groff/manual/groff.html#Pictures
