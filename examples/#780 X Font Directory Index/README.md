# #780 X Font Directory Index

Voce canonica `X Font Directory Index`, tipo `data`, language_id `208700028`.

Indice X Font Directory originale per un font BDF minimo, con alias `Hello, World!` e proprietà FAMILY_NAME contenente il saluto.

## Toolchain e riproduzione

mkfontdir / Xvfb / xlsfonts — 7.7+6build2; 1:7.7+6build3; 2:21.1.12-1ubuntu1.6. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Linux: xfonts-utils 1:7.7+6build3, x11-utils 7.7+6build2, Xvfb 2:21.1.12-1ubuntu1.6 e Python 3.12. Serve il font path di fallback /usr/share/fonts/X11/misc. Il driver copia font e alias nella directory output esterna; Xvfb viene avviato senza TCP e terminato alla fine.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
python3 verify.py <directory-font-output-esterna>
```

Risultato atteso: Indice generato uguale a fonts.dir, alias Hello, World! risolto da Xvfb e PASS.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

mkfontdir genera fonts.dir e viene confrontato con l’indice originale. Un vero Xvfb carica quel font path; xlsfonts risolve l’alias e legge i dati dal server. Il font ha un singolo glifo spazio: la semantica dichiarata riguarda indice, alias e proprietà, non il disegno delle lettere del saluto.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.x.org/docs/man/man.pdf](https://www.x.org/docs/man/man.pdf)
- [https://xorg.freedesktop.org/archive/X11R6.9.0/doc/PDF/fonts.pdf](https://xorg.freedesktop.org/archive/X11R6.9.0/doc/PDF/fonts.pdf)
