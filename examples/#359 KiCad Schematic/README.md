# #359 KiCad Schematic

Voce canonica `KiCad Schematic`, tipo `data`, language_id `622447435`.

Describe a KiCad schema without circuits with a visible text object containing greeting.

## Toolchain and reproduction

Required genuine toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

native format .kicad_sch 20230121 compatible with KiCad 7. The document contains original UUID, A4 sheet, empty lib_symbols and a text object.

Comando/procedura from the directory of the example, unless explicit indications:

```text
kicad-cli sch export svg --output build/ hello.kicad_sch; aprire in Schematic Editor e controllare il testo
```

Expected result: Charged diagram; SVG shows Hello, World!.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

The objective is the text of the scheme, not ERC of a circuit. Without loader/exporter KiCad, positive flags are not attributed to a generic S-expression parsing.

Remaining requirements:

- Native KiCad schematic loader/exporter is not available.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://dev-docs.kicad.org/en/file-formats/sexpr-schematic/](https://dev-docs.kicad.org/en/file-formats/sexpr-schematic/)
- [https://docs.kicad.org/7.0/en/eeschema/eeschema.html](https://docs.kicad.org/7.0/en/eeschema/eeschema.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.kicad_sch` | [hello.kicad_sch](hello.kicad_sch) created; verification pending |
| `.kicad_sym` | [hello.kicad_sym](variants/kicad-sym-fe143994/hello.kicad_sym) created; verification pending |
| `.sch` | [hello.sch](variants/sch-5766dac2/hello.sch) created; verification pending |
