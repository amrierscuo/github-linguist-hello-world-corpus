# #683 Stata

Voce canonica `Stata`, tipo `programming`, language_id `358`.

Run a do-file Stata with local macro and display.

## Toolchain and reproduction

Required genuine state compiler/runtime, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Requires State 18 or compatible with valid local license.

Comando/procedura from the directory of the example, unless explicit indications:

```text
stata -b do hello.do
```

Expected result: Hello, World! in the conformed result, according to the framework described.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Programma originale; interpreter proprietario unavailable.

Remaining requirements:

- Required stata toolchain and matching execution/format resources are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.stata.com/manuals/pdisplay.pdf](https://www.stata.com/manuals/pdisplay.pdf)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.do` | [hello.do](hello.do), [main.do](variants/doh-7967ee57/main.do) created; verification pending |
| `.ado` | [hello.ado](variants/ado-34dc7b88/hello.ado) created; verification pending |
| `.doh` | [hello.doh](variants/doh-7967ee57/hello.doh) created; verification pending |
| `.ihlp` | [hello.ihlp](variants/ihlp-05facafd/hello.ihlp) created; verification pending |
| `.mata` | [hello.mata](variants/mata-3f9d2836/hello.mata) created; verification pending |
| `.matah` | [hello.matah](variants/matah-70401489/hello.matah) created; verification pending |
| `.sthlp` | [hello.sthlp](variants/sthlp-90c77a77/hello.sthlp) created; verification pending |
