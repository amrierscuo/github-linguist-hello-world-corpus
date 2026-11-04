# #291 Harbour

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Run a Harbour program and write Hello, World! on stdout.

The Main procedure creates a local xBase variable and uses OutStd with hb_eol. The artifact is Harbour source, not a generic macro or Bash program.

## Toolchain and reproduction

Harbour hbmk2 o hbrun originali; versioni effettive da registrare

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
hbmk2 hello.hb -ohello
```

```text
./hello oppure hbrun hello.hb
```

## Expected result and status

stdout Hello, World! followed by the eol of the platform.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no native parser/compilatore/runtime performed for this item.

Impedimenti: Compiler/runtime Harbour non preparati; parsing ed esecuzione pendenti.

## Primary sources

- https://harbour.github.io/
- https://github.com/harbour/core/blob/master/utils/hbmk2/doc/hbmk2.en.md

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.hb` | [hello.hb](hello.hb) created; verification pending |
