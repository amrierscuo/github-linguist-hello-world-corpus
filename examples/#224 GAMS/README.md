# #224 GAMS

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Run GAMS and write Hello, World! in greeting.txt file.

The source uses a GAMS file, put and putclose. The result is a text file, not the output of a solver: an optimization model is not defined.

## Toolchain and reproduction

GAMS, installazione e licenza adatte; versione effettiva da registrare

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
gams hello.gms
```

## Expected result and status

greeting.txt contains Hello, World! followed by newline.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no native parser/compilatore/runtime performed for this item.

Impedimenti: Runtime proprietario GAMS non preparato; parsing ed esecuzione put restano pendenti.

## Primary sources

- https://www.gams.com/53/docs/UG_Put.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.gms` | [hello.gms](hello.gms) created; verification pending |
