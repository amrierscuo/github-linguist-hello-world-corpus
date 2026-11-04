# 0418: Markdown: `.workbook`

Ruolo: Xamarin Workbook testuale con YAML front matter e cella C#.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Python 3.13.9 + markdown-it-py 4.2.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Xamarin Workbooks storico: aprire hello.workbook, selezionare Console e valutare cella
```

Expected result: Hello, World! in the console

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.workbook`: `ae964d6e0f1ce395297aa04bbb4c591d7e1753a103460fcaad5c1344b85553cc`

Primary sources:

- https://github.com/microsoft/workbooks
- https://spec.commonmark.org/0.31.2/
- https://github.com/executablebooks/markdown-it-py
