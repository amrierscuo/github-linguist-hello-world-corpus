# #452 Mustache

Voce canonica `Mustache`, tipo `markup`, language_id `638334590`.

Render a parametric Mustache template and check the HTML scaling.

## Toolchain and reproduction

Existing Pystache Mustache compiler/renderer, 0.6.8. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Python e Pystache 0.6.8; installazione isolata sotto work.

Comando/procedura from the directory of the example, unless explicit indications:

```text
python verify.py hello.mustache
```

Expected result: Hello, World! and PASS of engine controls.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The real maker produces the greeting and the variant <Reader> is evacuated as expected; missing_tags strict.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://mustache.github.io/mustache.5.html](https://mustache.github.io/mustache.5.html)
- [https://pypi.org/project/pystache/](https://pypi.org/project/pystache/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mustache` | [hello.mustache](hello.mustache) verified |
