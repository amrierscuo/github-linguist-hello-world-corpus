# #778 Wren

Voce canonica `Wren`, tipo `programming`, language_id `713580619`.

Original Wren program that interpolates the name World and writes greeting with System.print.

## Toolchain and reproduction

Original Wren 0.4.0 C VM / GCC, gcc (Ubuntu 13.3.0-6ubuntu2 ~ 24.04.1 ) 13.3.0. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Official Sources Wren 0.4.0 from the release tagged; GCC 13.3.0. WREN and output are external directories for the example. host.c is a small original host for the API C Wren; all VM and the parser come from the original project.

Comando/procedura from the directory of the example, unless explicit indications:

```text
Linux: gcc -std=c99 -I<WREN>/src/include -I<WREN>/src/vm -I<WREN>/src/optional host.c <WREN>/src/vm/*.c <WREN>/src/optional/*.c -lm -o <output>/wrenhost
<output>/wrenhost hello.wren
```

Expected result: Hello, World! followed by newline; exit code 0.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Compilazione della VM ufficiale con i moduli optional originali, poi wrenInterpret sul sorgente .wren. Il codice di ritorno WREN_RESULT_SUCCESS e stdout sono verificati. Nessun interprete scritto ad hoc viene usato.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://wren.io/embedding/](https://wren.io/embedding/)
- [https://wren.io/interpolation.html](https://wren.io/interpolation.html)
- [https://github.com/wren-lang/wren/releases/tag/0.4.0](https://github.com/wren-lang/wren/releases/tag/0.4.0)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.wren` | [hello.wren](hello.wren) verified |
