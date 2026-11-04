# #064 BibTeX Style

Canonical entry from the corpus's `reference/languages.yml`. The reference and its order remain unchanged. The source was written for this example.

## Goal

Run an original BibTeX style that writes the title Hello, World! in the .bbl. file

hello.bst is a program in BibTeX's stack language: ENTRY, READ, ITERATE, write$ and newline$. input.bib and driver.aux are fixtures. The native warning about the undefined misc type is recorded. ITERATE calls write.greeting directly and does not dispatch by entry type.

## Toolchain and reproduction

BibTeX 0.99e; MiKTeX-BibTeX 4.2 (MiKTeX 25.12)

Command from the example folder, with the toolchain indicated available in the PATH. Run the build in a temporary copy to keep the generated files out of the corpus.

```text
bibtex driver
```

## Expected result and status

driver.bbl esattamente Hello, World! seguito da newline; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records actual commands, versioni/provenienza of the toolchain, output codes, stdout/stderr and SHA-256 of the proven sources.

## Primary sources

- https://ctan.org/pkg/bibtex
- https://mirrors.ctan.org/biblio/bibtex/base/btxhak.pdf

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.bst` | [hello.bst](hello.bst) verified |
