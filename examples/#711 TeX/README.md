# #711 TeX

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Valutare primitive TeX e scrivere Hello, World! nel terminale/log.

Il sorgente imposta esplicitamente le categorie delle graffe e usa immediate/write16. La prova INITEX non richiede formati, font o pagine; il risultato è il messaggio del motore.

## Toolchain e riproduzione

pdfTeX1.40.25 originale (TeX Live2023)

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
pdftex -ini -interaction=nonstopmode -halt-on-error hello.tex
```

## Risultato atteso e stato

Hello, World! nel terminale; exit0, nessuna pagina prodotta.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://tug.org/applications/pdftex/

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.tex` | [hello.tex](hello.tex), [generate.tex](variants/aux-48f45a54/generate.tex), [main.tex](variants/cls-699ea095/main.tex), [main.tex](variants/sty-186fa1b3/main.tex) creato, verifiche pendenti |
| `.aux` | [hello.aux](variants/aux-48f45a54/hello.aux) verificato |
| `.bbx` | [hello.bbx](variants/bbx-4927d20d/hello.bbx) creato, verifiche pendenti |
| `.cbx` | [hello.cbx](variants/cbx-d643bb7d/hello.cbx) creato, verifiche pendenti |
| `.cls` | [hello.cls](variants/cls-699ea095/hello.cls) creato, verifiche pendenti |
| `.dtx` | [hello.dtx](variants/dtx-41dec9a6/hello.dtx) creato, verifiche pendenti |
| `.ins` | [hello.ins](variants/ins-6ea4d746/hello.ins) creato, verifiche pendenti |
| `.lbx` | [hello.lbx](variants/lbx-5d3dde24/hello.lbx) creato, verifiche pendenti |
| `.ltx` | [hello.ltx](variants/ltx-ffb0c8cb/hello.ltx) creato, verifiche pendenti |
| `.mkii` | [hello.mkii](variants/mkii-db0f0c30/hello.mkii) creato, verifiche pendenti |
| `.mkiv` | [hello.mkiv](variants/mkiv-68523d59/hello.mkiv) creato, verifiche pendenti |
| `.mkvi` | [hello.mkvi](variants/mkvi-1dde5bac/hello.mkvi) creato, verifiche pendenti |
| `.sty` | [hello.sty](variants/sty-186fa1b3/hello.sty) creato, verifiche pendenti |
| `.toc` | [hello.toc](variants/toc-d72964f7/hello.toc) creato, verifiche pendenti |
