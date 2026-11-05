# #271 Graphviz (DOT)

## Latest recorded verification

Latest extension checks:
- `.gv`: Graphviz natively parsed and laid out the exact .gv file; the resulting SVG contains a text node exactly Hello, World!. Rendering stayed in files without a viewer. [Evidence](verification/native_20261105_batch_2e6776.json).

Voce canonica `Graphviz (DOT)`, tipo `data`, language_id `140`.

Render a DOT node with the Hello, World! label in a SVG produced by Graphviz.

## Toolchain and reproduction

Genuine Graphviz DOT parser and SVG layout maker, dot - graphviz version 2.43.0 ( 0 ). Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Graphviz 2.43.0 available on Ubuntu WSL2. The SVG product remains in build. verify_svg.py reads the XML of the real product.

Comando/procedura from the directory of the example, unless explicit indications:

```text
dot -Tsvg hello.dot -o build/hello.svg; python verify_svg.py build/hello.svg
```

Expected result: SVG valid with Hello, World! text; PASS.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The behavior verification confirms the presence of the greeting in the SVG text node; the log records its hash.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.graphviz.org/doc/info/lang.html](https://www.graphviz.org/doc/info/lang.html)
- [https://graphviz.org/docs/outputs/svg/](https://graphviz.org/docs/outputs/svg/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.dot` | [hello.dot](hello.dot) verified |
| `.gv` | [hello.gv](variants/ext-gv-2e6776/hello.gv) syntax and behavior verified |