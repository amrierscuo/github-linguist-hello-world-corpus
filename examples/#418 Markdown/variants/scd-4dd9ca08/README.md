# 0418: Markdown: `.scd`

Role: Manual scdoc: header mandatory name(section), not generic Markdown.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Python 3.13.9 + markdown-it-py 4.2.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
scdoc < hello.scd > hello.1
```

Expected result: Manpage with Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.scd`: `a9a70bfda1895c46f18bfb44e63289c3e5b8df63109bff49482c0ad21a22f28b`

Primary sources:

- https://git.sr.ht/~sircmpwn/scdoc/tree/master/item/scdoc.5.scd
- https://spec.commonmark.org/0.31.2/
- https://github.com/executablebooks/markdown-it-py
