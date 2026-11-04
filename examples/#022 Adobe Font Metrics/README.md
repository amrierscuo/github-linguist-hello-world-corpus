# #022 Adobe Font Metrics

Voce canonica: `Adobe Font Metrics`, tipo `data`, `language_id: 147198098`.
`hello.afm` contains original synthetic metrics in AFM 4.1 format for the ten
distinct glyphs used by `Hello, World!`. The glyph codes reconstruct the greeting;
the sum of the advances of the thirteen characters must be **7500 unità**.

## Toolchain and reproduction

verified su Windows x64 con Python **3.13.9** e **FontTools 4.60.1**.
From the directory of this example:

```powershell
python -m venv .venv
.venv/Scripts/python.exe -m pip install fonttools==4.60.1
.venv/Scripts/python.exe verify.py hello.afm
```

For a Python environment that already has FontTools 4.60.1: `python verify.py hello.afm`.
Expected result: `Hello, World!` followed by
`PASS: 10 glyph metrics; total advance = 7500 units; FontBBox = (0, 0, 600, 700)`.
The program uses `fontTools.afmLib.AFM` to read metrics and check name,
codes, widths and bounding box of the actual file.

## Status and evidence

Artefatto created; syntax **verified**; behavior **verified** con afmLib.
Real negative control: replacing the code of glyph H with `broken`, the parser
generate `fontTools.afmLib.error` and exit with 1. code The file is a demonstration of
metrics without contours; it is not a font to use to make greetings.
The verification covers the AFM subset supported by afmLib; the library declares
not to implement the entire Adobe specification. No residual requirement for this test.

Log: [fonttools.json](verification/fonttools.json), con comandi, output, versioni e
SHA-256. `path_normalization` describes the replacement of the machine paths;
the bytes of the sources and the results of the assertions remain unchanged.

## Official sources

- [FontTools afmLib: parser, accesso alle metriche e limiti](https://fonttools.readthedocs.io/en/latest/afmLib.html).

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.afm` | [hello.afm](hello.afm) verified |
