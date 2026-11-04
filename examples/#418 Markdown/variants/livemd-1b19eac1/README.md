# 0418: Markdown: `.livemd`

Role: Notebook Livebook Markdown with section and cell Elixir executable, not output recorded invented.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Python 3.13.9 + markdown-it-py 4.2.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Livebook: importare hello.livemd e valutare la cella
```

Expected result: Hello, World! in cell

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.livemd`: `7762dbb562980095688ba0cb1a3e2d32a94456bf9d09678c8ae8568649b3d676`

Primary sources:

- https://github.com/livebook-dev/livebook
- https://spec.commonmark.org/0.31.2/
- https://github.com/executablebooks/markdown-it-py
