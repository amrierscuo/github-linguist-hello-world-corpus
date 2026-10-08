# #256 Gnuplot

Interpretare uno script Gnuplot e produrre un grafico ASCII di y=x con titolo Hello, World!.

## Toolchain

gnuplot 6.0 patchlevel 0

## Comandi e procedura

gnuplot --version; gnuplot hello.gnuplot

## Risultato atteso

Exit 0; grafico ASCII contiene il titolo Hello, World! e la linea y=x.

## Stato

Sintassi e semantica verificate.

Lo script sceglie il terminale dumb e dimensioni definite; non richiede GUI o font esterni. Il runtime Gnuplot reale produce il grafico nel suo stdout, preservato nel log.

Verifica effettiva del 2026-10-08T12:17:31.366225+00:00 su WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://www.gnuplot.info/documentation.html](https://www.gnuplot.info/documentation.html)
- [https://gnuplot.sourceforge.net/docs/loc18701.html](https://gnuplot.sourceforge.net/docs/loc18701.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.gp` | [hello.gp](variants/ext-gp-2e6770/hello.gp) creato, verifiche pendenti |
| `.gnu` | [hello.gnu](variants/ext-gnu-2e676e75/hello.gnu) creato, verifiche pendenti |
| `.gnuplot` | [hello.gnuplot](hello.gnuplot) verificato |
| `.p` | [hello.p](variants/ext-p-2e70/hello.p) creato, verifiche pendenti |
| `.plot` | [hello.plot](variants/ext-plot-2e706c6f74/hello.plot) creato, verifiche pendenti |
| `.plt` | [hello.plt](variants/ext-plt-2e706c74/hello.plt) creato, verifiche pendenti |
