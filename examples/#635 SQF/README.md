# #635 SQF

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Run SQF and write Hello, World! in the log.

The local variable is formatted and written with diag_log; a generic parser C does not replace SQF.

## Toolchain and reproduction

VM SQF Arma, versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
Arma: [] execVM "hello.sqf"
```

## Expected result and status

Hello, World! in the SQF log.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Impedimenti: Runtime SQF/Arma unavailable; verification pending.

## Primary sources

- https://community.bohemia.net/wiki/diag_log

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.sqf` | [hello.sqf](hello.sqf), [main.sqf](variants/hqf-981d9d8f/main.sqf) created; verification pending |
| `.hqf` | [hello.hqf](variants/hqf-981d9d8f/hello.hqf) created; verification pending |
