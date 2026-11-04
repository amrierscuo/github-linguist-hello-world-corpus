# #153 D2

The canonical entry and order come from the corpus's `reference/languages.yml`. Sources and fixtures are original; any dumps or bundles come from the stated tools.

## Goal

Rendering a D2 node whose label is Hello, World!.

Il sorgente dichiara un nodo rectangle con una label. Il compilatore/renderer originale D2 interpreta il file e genera SVG; la label è testo effettivo dell’output XML. L’SVG generato non è incluso nel corpus.

## Toolchain and reproduction

D2 0.9.0, distribuzione ufficiale Linux amd64

Commands in the example folder with the toolchain available in PATH. Use a temporary copy: databases, objects, audio and other test outputs do not belong to the corpus.

```text
d2 hello.d2 hello.svg
```

```text
Controllare la label nell’SVG prodotto.
```

## Expected result and status

The maker ends exit 0 and SVG contains the Hello, World! text.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records versions and provenance, SHA-256 of the source, actual commands, exit, stdout and stderr normalized.

## Primary sources

- https://d2lang.com/tour/hello-world/
- https://d2lang.com/tour/text/
- https://github.com/d2lang/d2/releases/tag/v0.9.0

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.d2` | [hello.d2](hello.d2) verified |
