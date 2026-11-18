# #546 Portugol

## Verified on November 18, 2026

The published Portugol Studio JS tokenizer and bytecode compiler processed the original input. Its standalone VM executed the original program and the text output contained the exact greeting.

Run `node check.cjs <upstream source directory> tokenizer.js parser.js vm.js vmcompiler.js`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Run a Portugol2.0 program and write Hello, World!.

Il programma usa funcao inicio, cadeia e escreva con argomenti distinti. La forma è Portugol Studio, distinta da VisuAlg/Pascal.

## Toolchain and reproduction

Portugol Studio/UNIVALI originale; versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
Aprire hello.por in Portugol Studio ed eseguire inicio.
```

## Expected result and status

Hello, World! seguito da newline; exit0.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Commitments: Compiler/runtime Portugol Studio not prepared.

## Primary sources

- https://github.com/UNIVALI-LITE/Portugol-Studio
- https://univali-lite.github.io/Portugol-Studio/

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.por` | [hello.por](hello.por) Syntax and behavior verified |

</details>
