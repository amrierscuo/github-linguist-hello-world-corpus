# #359 KiCad Schematic

## Verified on November 18, 2026

The official KiCad CLI loaded the original source and used its headless plotter to generate an SVG containing the greeting and rendered vector paths.

Run `kicad-cli sch export svg --output ${SCRATCH}/359-hjpy0a34/out/ hello.kicad_sch`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_main.json).

[Earlier evidence](verification/native.json).

<details>
<summary>Earlier instructions and evidence</summary>

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
| `.kicad_sch` | [hello.kicad_sch](hello.kicad_sch) Syntax and behavior verified |
| `.kicad_sym` | [hello.kicad_sym](variants/kicad-sym-fe143994/hello.kicad_sym) created; verification pending |
| `.sch` | [hello.sch](variants/sch-5766dac2/hello.sch) created; verification pending |

</details>
