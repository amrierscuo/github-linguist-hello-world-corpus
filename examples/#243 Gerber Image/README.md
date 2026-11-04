# #243 Gerber Image

Render an original Gerber image representing Hello, World! with vector points.

## Toolchain

Python 3.13.9; PyGerber 2.4.3 genuine parser/renderer

## Commands and procedure

python -m pip install -r requirements.txt; python verify.py build/hello.png

## Expected result

Parser without errors; PNG reads Hello, World! with comma and exclamation point.

## Status

syntax and behavior verified.

I flash D03 usano un’apertura circolare di diametro 0.160 mm e coordinate millimetriche assolute 2.4. I glifi 5×7 in glyphs.json sono disegnati qui e trasformati in vettori originali; nessun font esterno. Parser e renderer PyGerber reali producono il PNG, ispezionato visivamente. L’immagine derivata rimane in work; non si dichiara un circuito o una fabbricazione PCB.

Actual verification of 2026-10-08T12:15:43.803158+00:00 on Windows x64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://www.ucamco.com/en/gerber/downloads](https://www.ucamco.com/en/gerber/downloads)
- [https://github.com/Argmaster/pygerber](https://github.com/Argmaster/pygerber)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.gbr` | [hello.gbr](hello.gbr) verified |
| `.cmp` | [hello.cmp](variants/ext-cmp-2e636d70/hello.cmp) created; verification pending |
| `.gbl` | [hello.gbl](variants/ext-gbl-2e67626c/hello.gbl) created; verification pending |
| `.gbo` | [hello.gbo](variants/ext-gbo-2e67626f/hello.gbo) created; verification pending |
| `.gbp` | [hello.gbp](variants/ext-gbp-2e676270/hello.gbp) created; verification pending |
| `.gbs` | [hello.gbs](variants/ext-gbs-2e676273/hello.gbs) created; verification pending |
| `.gko` | [hello.gko](variants/ext-gko-2e676b6f/hello.gko) created; verification pending |
| `.gml` | [hello.gml](variants/ext-gml-2e676d6c/hello.gml) created; verification pending |
| `.gpb` | [hello.gpb](variants/ext-gpb-2e677062/hello.gpb) created; verification pending |
| `.gpt` | [hello.gpt](variants/ext-gpt-2e677074/hello.gpt) created; verification pending |
| `.gtl` | [hello.gtl](variants/ext-gtl-2e67746c/hello.gtl) created; verification pending |
| `.gto` | [hello.gto](variants/ext-gto-2e67746f/hello.gto) created; verification pending |
| `.gtp` | [hello.gtp](variants/ext-gtp-2e677470/hello.gtp) created; verification pending |
| `.gts` | [hello.gts](variants/ext-gts-2e677473/hello.gts) created; verification pending |
| `.ncl` | [hello.ncl](variants/ext-ncl-2e6e636c/hello.ncl) created; verification pending |
| `.sol` | [hello.sol](variants/ext-sol-2e736f6c/hello.sol) created; verification pending |
