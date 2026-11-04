# #226 GCC Machine Description

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Define 13 constant GCC Machine Description that encode Hello, World! bytes.

The file uses the documented MD construct called_constants, without inventing instruction patterns for a CPU. Greeting is contained in the values of the constants. genconstants is an internal tool of the GCC build; an installed gcc compiler is not equivalent to the MD parser.

## Toolchain and reproduction

Genconstants internal generators of a build tree GCC; actual version to record

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
genconstants hello.md > greeting-constants.h
```

```text
Controllare CORPUS_CHAR_00..12 nell’header generato.
```

## Expected result and status

Le 13 macro emesse hanno i valori ASCII 72,101,108,108,111,44,32,87,111,114,108,100,33.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no native parser/compilatore/runtime performed for this item.

Commitments: A build tree GCC with genconstants generator is not available; the MD file has not been analyzed by the original generator.

## Primary sources

- https://gcc.gnu.org/onlinedocs/gcc-14.3.0/gccint/Machine-Desc.html
- https://gcc.gnu.org/onlinedocs/gcc-7.3.0/gccint/Constant-Definitions.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.md` | [hello.md](hello.md) created; verification pending |
