# #779 X BitMap

Voce canonica `X BitMap`, tipo `data`, language_id `782911107`.

Original XBM image from 104 × 1 pixels: the bits of the row codify the 13 byte ASCII of `Hello, World!`, in the LSB order provided by the bitmap X format.

## Toolchain and reproduction

Pillow / Python 3.13.9, 12.0.0. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Python 3.13.9 e Pillow 12.0.0 in ambiente isolato.

Comando/procedura from the directory of the example, unless explicit indications:

```text
python verify.py
```

Expected result: Image XBM 104 × 1 uploaded, payload Hello, World! and PASS.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Pillow really plays XBM and uploads the image. The driver reassembles the bytes from the uploaded pixels and controls the payload. The goal is a binary encoding in pixels, not the graphic rendering of visible letters.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#xbm](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#xbm)
- [https://www.x.org/releases/current/doc/libX11/libX11/libX11.html](https://www.x.org/releases/current/doc/libX11/libX11/libX11.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.xbm` | [hello.xbm](hello.xbm) verified |
