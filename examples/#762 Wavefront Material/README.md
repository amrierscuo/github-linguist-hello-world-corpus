# #762 Wavefront Material

Voce canonica `Wavefront Material`, tipo `data`, language_id `392`.

Materiale Wavefront MTL originale con nome `Hello, World!` e colore diffuso RGB (0.8, 0.4, 0.1).

## Toolchain and reproduction

trimesh / Python 3.13.9, 5.1.1. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Python 3.13.9, trimesh 5.1.1 and NumPy. Install the libraries in an isolated environment; the test uses the MTL/OBJ loader of the trimesh project.

Comando/procedura from the directory of the example, unless explicit indications:

```text
python verify.py
```

Expected result: Hello, World!, followed by PASS; name, color or geometry correspond to the original model.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The existing parser reads the native file. The original assertions control the name and the data model: color for MTL; geometry, bounds and reference to the material for OBJ. The stated objective is the loaded model, not a 3D. rendering.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://trimesh.org/trimesh.exchange.obj.html](https://trimesh.org/trimesh.exchange.obj.html)
- [https://paulbourke.net/dataformats/obj/](https://paulbourke.net/dataformats/obj/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mtl` | [hello.mtl](hello.mtl) verified |
