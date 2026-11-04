# #254 Glyph Bitmap Distribution Format

Upload an original BDF font and rasterize all Hello, World! characters.

## Toolchain

Python 3.13.9; freetype-py 2.5.1 genuine FreeType rasterizer

## Commands and procedure

python -m pip install -r requirements.txt; python verify.py build/hello.png

## Expected result

FreeType charge BDF; each string character has bitmap 5 × 7 correct; PNG reads greeting.

## Status

syntax and behavior verified.

hello.bdf definisce dieci glifi 5×7 originali, inclusi spazio e punteggiatura. glyphs.json esplicita il disegno per il confronto. Il driver BDF di FreeType restituisce le bitmap reali, confrontate pixel per pixel per ogni lettera; il risultato è stato anche ispezionato. Nessun font redistribuito; PNG derivato solo in work.

Actual verification of 2026-10-08T12:15:39.471165+00:00 on Windows x64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://www.x.org/releases/X11R7.0/doc/PDF/bdf.pdf](https://www.x.org/releases/X11R7.0/doc/PDF/bdf.pdf)
- [https://freetype.org/freetype2/docs/reference/ft2-bdf_fonts.html](https://freetype.org/freetype2/docs/reference/ft2-bdf_fonts.html)
- [https://github.com/rougier/freetype-py](https://github.com/rougier/freetype-py)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.bdf` | [hello.bdf](hello.bdf) verified |
