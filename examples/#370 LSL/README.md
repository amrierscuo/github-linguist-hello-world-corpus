# #370 LSL

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Al ricevimento di state_entry, comunicare Hello, World! al proprietario tramite LSL.

The default state contains a state_entry event and calls llOwnerSay; the greeting is executable code for the LSL runtime.

## Toolchain and reproduction

Second Life/LSL o runtime compatibile; versione da registrare

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
Caricare hello.lsl come script di un oggetto e avviare state_entry.
```

## Expected result and status

Owner's chat contains Hello, World!.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no native parser/compilatore/runtime performed for this item.

Commitments: Runtime LSL unavailable; no access to the online platform.

## Primary sources

- https://wiki.secondlife.com/wiki/LSL_Portal
- https://wiki.secondlife.com/wiki/LlOwnerSay

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.lsl` | [hello.lsl](hello.lsl) created; verification pending |
| `.lslp` | [hello.lslp](variants/lslp-5b201320/hello.lslp) created; verification pending |
