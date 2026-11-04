# #222 G-code

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Define the LCD Hello, World! message by M117 in the Marlin dialect, without movements.

The original gcodeparser parser recognizes M117 but treats the message letters as parameters: this lexical test does not validate the complete dialect. No command has been sent to serial machines or ports.

## Toolchain and reproduction

Marlin M117; parser Python gcodeparser 0.3.0 provato offline

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
Solo offline: analizzare hello.gcode con un parser che supporti il testo libero Marlin M117.
```

## Expected result and status

The M117 command has the Hello, World! message; it does not contain movement instructions.

Artifact created: yes. syntax verified: no. behavior verified: no.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

Commitments: The available parser does not properly support the free text topic M117; syntax of the dialect and LCD message remain unchecked.

## Primary sources

- https://marlinfw.org/docs/gcode/M117.html
- https://github.com/AndyEveritt/GcodeParser

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.g` | [hello.g](variants/ext-g-2e67/hello.g) created; verification pending |
| `.cnc` | [hello.cnc](variants/ext-cnc-2e636e63/hello.cnc) created; verification pending |
| `.gco` | [hello.gco](variants/ext-gco-2e67636f/hello.gco) created; verification pending |
| `.gcode` | [hello.gcode](hello.gcode) created; verification pending |
