# #157 DTrace

The canonical entry and order come from the corpus's `reference/languages.yml`. Sources and fixtures are original; any dumps or bundles come from the stated tools.

## Goal

Perform a DTrace BEGIN clause that prints Hello, World! and ends immediately.

The .d extension here contains the D language of DTrace, distinct from the D-general language. The only probe is:: BEGIN is performed at startup; no events or data are collected from other processes.

## Toolchain and reproduction

DTrace originale su sistema supportato; versione effettiva da registrare

Commands in the example folder with the toolchain available in PATH. Use a temporary copy: databases, objects, audio and other test outputs do not belong to the corpus.

```text
dtrace -e -s hello.d
```

```text
dtrace -s hello.d
```

## Expected result and status

stdout Hello, World! followed by newline; exit( 0) closes the DTrace program.

Artifact created: yes. syntax verified: no. behavior verified: no.

The source is documented; native parser/compilatore/runtime has not been performed for this item.

Commitments: Runtime DTrace and kernel support not prepared in this environment; compilation and BEGIN probe remain pending.

## Primary sources

- https://docs.oracle.com/cd/F61410_01/dtrace-guide/OL-DTRACE-GUIDE.pdf

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.d` | [hello.d](hello.d) created; verification pending |
