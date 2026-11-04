# #269 Graph Modeling Language

Voce canonica `Graph Modeling Language`, tipo `data`, language_id `138`.

Represent a direct GML graph with a knot labeled by greeting.

## Toolchain and reproduction

NetworkX native GML reader, 3.5. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

NetworkX 3.5 on Python 3.13.9. read_gml(label=None) retains the numerical id and label law as an attribute.

Comando/procedura from the directory of the example, unless explicit indications:

```text
python -m pip install networkx==3.5; python verify.py hello.gml
```

Expected result: Hello, World! and PASS of graph fields.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The existing reader analyzes the format and control checks only one 0 node, direct graph, zero strings and exact label. No GML parser homemade is used.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://networkx.org/documentation/stable/reference/readwrite/generated/networkx.readwrite.gml.read_gml.html](https://networkx.org/documentation/stable/reference/readwrite/generated/networkx.readwrite.gml.read_gml.html)
- [https://github.com/networkx/networkx](https://github.com/networkx/networkx)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.gml` | [hello.gml](hello.gml) verified |
