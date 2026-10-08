# #243 Gerber Image

Renderizzare un’immagine Gerber originale che rappresenta Hello, World! con punti vettoriali.

## Toolchain

Python 3.13.9; PyGerber 2.4.3 genuine parser/renderer

## Comandi e procedura

python -m pip install -r requirements.txt; python verify.py build/hello.png

## Risultato atteso

Parser senza errori; PNG legge Hello, World! con virgola e punto esclamativo.

## Stato

Sintassi e semantica verificate.

I flash D03 usano un’apertura circolare di diametro 0.160 mm e coordinate millimetriche assolute 2.4. I glifi 5×7 in glyphs.json sono disegnati qui e trasformati in vettori originali; nessun font esterno. Parser e renderer PyGerber reali producono il PNG, ispezionato visivamente. L’immagine derivata rimane in work; non si dichiara un circuito o una fabbricazione PCB.

Verifica effettiva del 2026-10-08T12:15:43.803158+00:00 su Windows x64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://www.ucamco.com/en/gerber/downloads](https://www.ucamco.com/en/gerber/downloads)
- [https://github.com/Argmaster/pygerber](https://github.com/Argmaster/pygerber)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.gbr` | [hello.gbr](hello.gbr) verificato |
| `.cmp` | [hello.cmp](variants/ext-cmp-2e636d70/hello.cmp) creato, verifiche pendenti |
| `.gbl` | [hello.gbl](variants/ext-gbl-2e67626c/hello.gbl) creato, verifiche pendenti |
| `.gbo` | [hello.gbo](variants/ext-gbo-2e67626f/hello.gbo) creato, verifiche pendenti |
| `.gbp` | [hello.gbp](variants/ext-gbp-2e676270/hello.gbp) creato, verifiche pendenti |
| `.gbs` | [hello.gbs](variants/ext-gbs-2e676273/hello.gbs) creato, verifiche pendenti |
| `.gko` | [hello.gko](variants/ext-gko-2e676b6f/hello.gko) creato, verifiche pendenti |
| `.gml` | [hello.gml](variants/ext-gml-2e676d6c/hello.gml) creato, verifiche pendenti |
| `.gpb` | [hello.gpb](variants/ext-gpb-2e677062/hello.gpb) creato, verifiche pendenti |
| `.gpt` | [hello.gpt](variants/ext-gpt-2e677074/hello.gpt) creato, verifiche pendenti |
| `.gtl` | [hello.gtl](variants/ext-gtl-2e67746c/hello.gtl) creato, verifiche pendenti |
| `.gto` | [hello.gto](variants/ext-gto-2e67746f/hello.gto) creato, verifiche pendenti |
| `.gtp` | [hello.gtp](variants/ext-gtp-2e677470/hello.gtp) creato, verifiche pendenti |
| `.gts` | [hello.gts](variants/ext-gts-2e677473/hello.gts) creato, verifiche pendenti |
| `.ncl` | [hello.ncl](variants/ext-ncl-2e6e636c/hello.ncl) creato, verifiche pendenti |
| `.sol` | [hello.sol](variants/ext-sol-2e736f6c/hello.sol) creato, verifiche pendenti |
