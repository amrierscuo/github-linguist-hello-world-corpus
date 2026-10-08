# #254 Glyph Bitmap Distribution Format

Caricare un font BDF originale e rasterizzare tutti i caratteri di Hello, World!.

## Toolchain

Python 3.13.9; freetype-py 2.5.1 genuine FreeType rasterizer

## Comandi e procedura

python -m pip install -r requirements.txt; python verify.py build/hello.png

## Risultato atteso

FreeType carica BDF; ogni carattere della stringa ha bitmap 5×7 corretta; PNG legge il saluto.

## Stato

Sintassi e semantica verificate.

hello.bdf definisce dieci glifi 5×7 originali, inclusi spazio e punteggiatura. glyphs.json esplicita il disegno per il confronto. Il driver BDF di FreeType restituisce le bitmap reali, confrontate pixel per pixel per ogni lettera; il risultato è stato anche ispezionato. Nessun font redistribuito; PNG derivato solo in work.

Verifica effettiva del 2026-10-08T12:15:39.471165+00:00 su Windows x64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://www.x.org/releases/X11R7.0/doc/PDF/bdf.pdf](https://www.x.org/releases/X11R7.0/doc/PDF/bdf.pdf)
- [https://freetype.org/freetype2/docs/reference/ft2-bdf_fonts.html](https://freetype.org/freetype2/docs/reference/ft2-bdf_fonts.html)
- [https://github.com/rougier/freetype-py](https://github.com/rougier/freetype-py)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bdf` | [hello.bdf](hello.bdf) verificato |
