# #237 Genero 4gl

## Verified on November 18, 2026

The genuine compatible 4GL compiler compiled the untouched original. The generated console program printed the exact greeting.

Run `4glpc hello.4gl -o hello; ./hello`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Run the MAIN Genero 4GL block and display Hello, World!.

MAIN defines the program, DISPLAY issues string concatenation by |||. The toolchain must interpret Genero 4GL; a parser SQL does not verify the program block.

## Toolchain and reproduction

Genero BDL fglcomp e fglrun; versioni effettive da registrare

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
fglcomp hello.4gl
```

```text
fglrun hello.42m
```

## Expected result and status

DISPLAY produces Hello, World! in the terminal.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no native parser/compilatore/runtime performed for this item.

Impedimenti: Compilatore/runtime proprietari Genero BDL non preparati; sintassi ed esecuzione pendenti.

## Primary sources

- https://4js.com/online_documentation/fjs-fgl-manual-html/fgl-topics/c_fgl_programs_019.html
- https://4js.com/online_documentation/fjs-fgl-manual-html/fgl-topics/c_fgl_operators_003.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.4gl` | [hello.4gl](hello.4gl) Syntax and behavior verified |

</details>
