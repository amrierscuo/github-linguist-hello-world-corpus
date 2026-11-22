# #376 Lasso

## Verified on November 22, 2026

The native Lasso compiler accepted the original hello.lasso9 and GCC linked the resulting object. The offline executable wrote the greeting Hello, World! on one line followed by two empty lines. The process remained active after the greeting and the harness stopped it after 30 seconds (exit 124).

Run `lassoc -O -app -n -obj -o hello.a.o hello.lasso9; gcc -no-pie -o hello hello.a.o -llasso9_runtime; LASSO9_HOME=<vendor Lasso home> ./hello`.

[Commands, toolchain, output and SHA-256](verification/native_20261122_wave800_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Interpretare Lasso9 e scrivere Hello, World! su stdout.

The block <?lasso declares local audience; stdoutnl writes the result of the concatenation.

## Toolchain and reproduction

Lasso9 originale; versione da registrare

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
lasso9 hello.lasso9
```

## Expected result and status

stdout Hello, World! seguito da newline.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no native parser/compilatore/runtime performed for this item.

Impedimenti: Runtime Lasso9 unavailable; verification pending.

## Primary sources

- https://lassoguide.com/operations/command-line-tools.html
- https://lassoguide.com/language/variables.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.lasso` | [hello.lasso](variants/lasso-86f92243/hello.lasso) created; verification pending |
| `.las` | [hello.las](variants/las-2efc32e6/hello.las) created; verification pending |
| `.lasso8` | [hello.lasso8](variants/lasso8-e15216c5/hello.lasso8) created; verification pending |
| `.lasso9` | [hello.lasso9](hello.lasso9) Syntax and behavior verified |

</details>
