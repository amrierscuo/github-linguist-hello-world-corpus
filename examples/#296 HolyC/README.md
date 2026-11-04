# #296 HolyC

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Caricare codice HolyC in TempleOS e stampare Hello, World! con Print.

The top-level code calls Greeting(), as predicted by HolyC; does not use a main C. The %s format is interpreted by the native TempleOS Print.

## Toolchain and reproduction

TempleOS/HolyC originale; versione effettiva da registrare

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
Nel terminale TempleOS: #include "hello.hc"
```

## Expected result and status

Print emette Hello, World! seguito da newline.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no native parser/compilatore/runtime performed for this item.

Commitments: TempleOS and compiler/runtime HolyC not available; no verification with GCC replacement.

## Primary sources

- https://raw.githubusercontent.com/cia-foundation/TempleOS/archive/Doc/HolyC.DD
- https://github.com/cia-foundation/TempleOS/tree/archive

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.hc` | [hello.hc](hello.hc) created; verification pending |
