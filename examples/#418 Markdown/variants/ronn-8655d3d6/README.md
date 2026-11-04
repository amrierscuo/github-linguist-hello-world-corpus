# 0418: Markdown: `.ronn`

Ruolo: Documento Ronn con intestazione name(section) e sezioni man.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Python 3.13.9 + markdown-it-py 4.2.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
ronn --roff hello.ronn
```

Expected result: Manpage with Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.ronn`: `6106b50a78d01bc5c119d6d5531f5e981057352825fc561600b1ab42698332b1`

Primary sources:

- https://github.com/rtomayko/ronn
- https://spec.commonmark.org/0.31.2/
- https://github.com/executablebooks/markdown-it-py
