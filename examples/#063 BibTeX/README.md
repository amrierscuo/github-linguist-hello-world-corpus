# #063 BibTeX

Canonical entry from the corpus's `reference/languages.yml`. The reference and its order remain unchanged. The source was written for this example.

## Goal

Read a bibliographical entry whose title is Hello, World! and generate bibliography.

hello.bib is the BibTeX database. driver.aux specific quote, database and plain standard style. behavior verified is the title generation in .bbl file, not a PDF LaTeX compilation.

## Toolchain and reproduction

BibTeX 0.99e; MiKTeX-BibTeX 4.2 (MiKTeX 25.12); plain.bst

Command from the example folder, with the toolchain indicated available in the PATH. Run the build in a temporary copy to keep the generated files out of the corpus.

```text
bibtex driver
```

## Expected result and status

driver.bbl contains the title { Hello, World! }; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records actual commands, versioni/provenienza of the toolchain, output codes, stdout/stderr and SHA-256 of the proven sources.

## Primary sources

- https://ctan.org/pkg/bibtex
- https://mirrors.ctan.org/biblio/bibtex/base/btxdoc.pdf

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.bib` | [hello.bib](hello.bib) verified |
| `.bibtex` | [hello.bibtex](variants/ext-bibtex-2e626962746578/hello.bibtex) created; verification pending |
