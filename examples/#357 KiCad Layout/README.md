# #357 KiCad Layout

Voce canonica `KiCad Layout`, tipo `data`, language_id `187`.

Describe a KiCad card with rectangular edge and Hello, World! text on the front screen.

## Toolchain and reproduction

Required genuine toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

native .kicad_pcb 20221018 version compatible with KiCad 7. The file contains two layers copper, silkscreen and Edge.Cuts; no component or routing is necessary for the objective.

Comando/procedura from the directory of the example, unless explicit indications:

```text
kicad-cli pcb export svg --layers F.Silkscreen,Edge.Cuts --output build/ hello.kicad_pcb; aprire la scheda in PCB Editor e controllare testo e bordo
```

Expected result: KiCad loads the card and SVG shows rectangular edge and Hello, World!.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

The description is original and follows the documentation of the format; the toolchain CAD is not available and is not replaced by a generic parser S-expression.

Remaining requirements:

- Native KiCad PCB loader/exporter is not available.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://dev-docs.kicad.org/en/file-formats/sexpr-pcb/](https://dev-docs.kicad.org/en/file-formats/sexpr-pcb/)
- [https://docs.kicad.org/7.0/en/pcbnew/pcbnew.html](https://docs.kicad.org/7.0/en/pcbnew/pcbnew.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.kicad_pcb` | [hello.kicad_pcb](hello.kicad_pcb) created; verification pending |
| `.kicad_mod` | [hello.kicad_mod](variants/kicad-mod-72f4d4f5/hello.kicad_mod) created; verification pending |
| `.kicad_wks` | [hello.kicad_wks](variants/kicad-wks-ff39775a/hello.kicad_wks) created; verification pending |
