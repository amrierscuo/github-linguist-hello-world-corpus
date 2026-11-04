# #426 Mermaid

Analyze a Mermaid diagram and read the node greeting label from the parser database.

Canonical type `markup`, language_id `385992043`.

Suggested toolchain: Node.js 22, Mermaid and jsdom.

From the example directory:

```sh
node verify.cjs
```

Expected result: a greeting node with Hello, World! text; stdout greeting and LF.

The goal is to interpret the graph and label with the original engine. It does not certify SVG geometry or rendering of a browser.

Recorded status: syntax verified; behavior verified. Toolchain: Node.js 22.20.0 + Mermaid 11.12.0 + jsdom 26.1.0. [Log](verification/result.json).

Sources:

- [Mermaid — flowchart](https://mermaid.js.org/syntax/flowchart.html)
- [Mermaid — API](https://mermaid.js.org/config/usage.html)

Install the dependencies in a separate directory:

```sh
npm install --ignore-scripts --no-audit --no-fund mermaid@11.12.0 jsdom@26.1.0
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mmd` | [hello.mmd](hello.mmd) verified |
| `.mermaid` | [hello.mermaid](variants/mermaid-4637b47f/hello.mermaid) created; verification pending |
