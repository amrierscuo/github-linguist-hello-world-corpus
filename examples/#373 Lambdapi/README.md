# #373 Lambdapi

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Define in Lambdapi a list of13natural numbers coding ASCII Hello, World!.

Nat, zero, succ and List are declared in the file, without implied libraries. n32 etc. define unari numbers; greeting concatena the cons/nil. type and compute values require the original processing engine.

## Toolchain and reproduction

Lambdapi originale; versione da registrare

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
lambdapi check hello.lp
```

```text
lambdapi check hello.lp
```

## Expected result and status

greeting è ben tipato; compute normalizza i13naturali72,101,108,108,111,44,32,87,111,114,108,100,33.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no native parser/compilatore/runtime performed for this item.

Impedimenti: Lambdapi/ambiente OCaml non preparati; controllo del tipo e normalizzazione pendenti.

## Primary sources

- https://lambdapi.readthedocs.io/en/stable/commands.html
- https://lambdapi.readthedocs.io/en/stable/queries.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.lp` | [hello.lp](hello.lp) created; verification pending |
