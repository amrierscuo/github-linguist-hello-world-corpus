# #711 TeX

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Evaluate primitive TeX and write Hello, World! in terminale/log.

The source explicitly sets the categories of the scratches and uses immediate/write16. The INITEX test does not require formats, fonts or pages; the result is the engine message.

## Toolchain and reproduction

pdfTeX1.40.25 originale (TeX Live2023)

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
pdftex -ini -interaction=nonstopmode -halt-on-error hello.tex
```

## Expected result and status

Hello, World! in the terminal; exit0, no page produced.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://tug.org/applications/pdftex/

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.tex` | [hello.tex](hello.tex), [generate.tex](variants/aux-48f45a54/generate.tex), [main.tex](variants/cls-699ea095/main.tex), [main.tex](variants/sty-186fa1b3/main.tex) created; verification pending |
| `.aux` | [hello.aux](variants/aux-48f45a54/hello.aux) verified |
| `.bbx` | [hello.bbx](variants/bbx-4927d20d/hello.bbx) created; verification pending |
| `.cbx` | [hello.cbx](variants/cbx-d643bb7d/hello.cbx) created; verification pending |
| `.cls` | [hello.cls](variants/cls-699ea095/hello.cls) created; verification pending |
| `.dtx` | [hello.dtx](variants/dtx-41dec9a6/hello.dtx) created; verification pending |
| `.ins` | [hello.ins](variants/ins-6ea4d746/hello.ins) created; verification pending |
| `.lbx` | [hello.lbx](variants/lbx-5d3dde24/hello.lbx) created; verification pending |
| `.ltx` | [hello.ltx](variants/ltx-ffb0c8cb/hello.ltx) created; verification pending |
| `.mkii` | [hello.mkii](variants/mkii-db0f0c30/hello.mkii) created; verification pending |
| `.mkiv` | [hello.mkiv](variants/mkiv-68523d59/hello.mkiv) created; verification pending |
| `.mkvi` | [hello.mkvi](variants/mkvi-1dde5bac/hello.mkvi) created; verification pending |
| `.sty` | [hello.sty](variants/sty-186fa1b3/hello.sty) created; verification pending |
| `.toc` | [hello.toc](variants/toc-d72964f7/hello.toc) created; verification pending |
