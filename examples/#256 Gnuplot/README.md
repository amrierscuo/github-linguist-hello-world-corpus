# #256 Gnuplot

Play a Gnuplot script and produce a ASCII graph of y=x with title Hello, World!.

## Toolchain

gnuplot 6.0 patchlevel 0

## Commands and procedure

gnuplot --version; gnuplot hello.gnuplot

## Expected result

Exit 0; ASCII chart contains the title Hello, World! and the y=x line.

## Status

syntax and behavior verified.

The script chooses the dumb terminal and defined dimensions; it does not require GUI or external fonts. The real Gnuplot runtime produces the graph in its stdout, preserved in the log.

Actual verification of 2026-10-08T12:17:31.366225+00:00 on WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://www.gnuplot.info/documentation.html](https://www.gnuplot.info/documentation.html)
- [https://gnuplot.sourceforge.net/docs/loc18701.html](https://gnuplot.sourceforge.net/docs/loc18701.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.gp` | [hello.gp](variants/ext-gp-2e6770/hello.gp) created; verification pending |
| `.gnu` | [hello.gnu](variants/ext-gnu-2e676e75/hello.gnu) created; verification pending |
| `.gnuplot` | [hello.gnuplot](hello.gnuplot) verified |
| `.p` | [hello.p](variants/ext-p-2e70/hello.p) created; verification pending |
| `.plot` | [hello.plot](variants/ext-plot-2e706c6f74/hello.plot) created; verification pending |
| `.plt` | [hello.plt](variants/ext-plt-2e706c74/hello.plt) created; verification pending |
