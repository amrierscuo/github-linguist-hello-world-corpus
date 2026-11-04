# #693 Sweave

Voce canonica `Sweave`, tipo `prose`, language_id `558779190`.

Run the chunk R of a Sweave document and produce greeting in the generated LaTeX.

## Toolchain and reproduction

Original R Sweave document engine, R version 4.3.3 ( 2024-02-29 ) -- "Angel Food Cake". Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

GNU R4.3.3 and original Sweave. The log records R_HOME and relocated distribution libraries.

Comando/procedura from the directory of the example, unless explicit indications:

```text
R --vanilla --slave -e 'utils::Sweave("hello.rnw",output="build/hello.tex")'
```

Expected result: Hello, World! in the conformed result, according to the framework described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

R performs cat in the chunk results=tex; the generated document contains the exact greeting. Scope: Sweave and LaTeX generated, without compilazione/impaginazione TeX.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://stat.ethz.ch/R-manual/R-devel/library/utils/html/Sweave.html](https://stat.ethz.ch/R-manual/R-devel/library/utils/html/Sweave.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.rnw` | [hello.rnw](hello.rnw) verified |
