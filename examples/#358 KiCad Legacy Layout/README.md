# #358 KiCad Legacy Layout

Voce canonica `KiCad Legacy Layout`, tipo `data`, language_id `140848857`.

Describe in the legacy format KiCad .brd a text of Hello, World! silkscreen.

## Toolchain and reproduction

Required genuine toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Format PCBNEW - BOARD Version 1, coordinates in 1/10000 inch. The text is a $ TEXTPCB object on the 21 legacy layer; the file ends with $EndBOARD.

Comando/procedura from the directory of the example, unless explicit indications:

```text
PCB Editor KiCad: aprire/importare hello.brd in una copia di lavoro, salvare come .kicad_pcb ed esportare SVG della serigrafia frontale
```

Expected result: Successful native import; frontal serigraphy shows Hello, World!.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

This is the legacy format, distinct from the modern S-expression artifact. The greeting is the Te field of the true textual object. Importatore/renderer KiCad absents; the flags remain false.

Remaining requirements:

- Native KiCad legacy PCB importer/renderer is not available.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://dev-docs.kicad.org/en/file-formats/legacy-pcb/](https://dev-docs.kicad.org/en/file-formats/legacy-pcb/)
- [https://docs.kicad.org/9.0/en/kicad/kicad.html](https://docs.kicad.org/9.0/en/kicad/kicad.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.brd` | [hello.brd](hello.brd) created; verification pending |
