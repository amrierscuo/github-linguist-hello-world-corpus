# #200 FIGlet Font

Analyze an original FIGlet font to a row and make Hello, World! while maintaining the individual glifi.

Canonical type `data`, language_id `686129783`.

Suggested toolchain: Python 3 and pyfiglet.

From the example directory:

```sh
python verify.py
```

Expected result: loaded font, 1 height, exact rendering `Hello, World!\n`.

The glyphs and the commentary of the font are original: an external font is not redistributed. There are 95 mandatory ASCII characters and the seven German characters provided by the format; full-width layout without smushing.

Recorded status: syntax verified; behavior verified. Toolchain: Python 3.13.9 + pyfiglet 1.0.4. See [log](verification/verification.log).

Sources of linguaggio/formato and original implementations:

- [FIGfont — specifica originale](https://github.com/cmatsuoka/figlet/blob/master/figfont.txt)
- [pyfiglet — parser e renderer](https://github.com/pwaller/pyfiglet)

Install the dependencies in a separate directory:

```sh
python -m pip install pyfiglet==1.0.4
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.flf` | [greeting.flf](greeting.flf) verified |
