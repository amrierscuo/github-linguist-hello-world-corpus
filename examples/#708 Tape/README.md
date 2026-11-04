# #708 Tape

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Describe a terminal recording with echo Hello, World! in the language Tape of VHS.

Tape .tape è il linguaggio di registrazione di VHS nella voce canonica. Il parser originale valida il file senza avviare una registrazione.

## Toolchain and reproduction

VHS0.12.1 originale

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
vhs validate hello.tape; vhs hello.tape
```

## Expected result and status

valid tape; waiting recording shows the command and Hello, World!.

Artifact created: yes. syntax verified: yes. behavior verified: no.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

Commitments: Registrazione/controllo of the video not executed; requires ttyd, ffmpeg and compatible browser.

## Primary sources

- https://github.com/charmbracelet/vhs

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.tape` | [hello.tape](hello.tape) syntax verified |
