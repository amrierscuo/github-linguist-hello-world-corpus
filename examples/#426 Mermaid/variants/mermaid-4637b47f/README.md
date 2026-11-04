# 0426: Mermaid: `.mermaid`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#426 Mermaid/hello.mmd.

Required toolchain: Node.js 22.20.0 + Mermaid 11.12.0 + jsdom 26.1.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.mermaid; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: a greeting node with Hello, World! text; stdout greeting and LF.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.mermaid`: `81d7210bdc34658684885842d1f77c662eddbd92474995475e1df6c91fd7aa5c`
- `verify.cjs`: `aa18c79b58a45b7a4bf1bb3c42aa3ba88deed9ce1a48c4122c60ab2d72591e5f`

Primary sources:

- https://mermaid.js.org/syntax/flowchart.html
- https://mermaid.js.org/config/usage.html
