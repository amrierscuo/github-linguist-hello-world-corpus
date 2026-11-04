# #629 SAS

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Run a DATA step SAS and write Hello, World! in the log.

DATA _NULL_ avoids creating dataset; the string has declared length13 and PUT writes the calculated value.

## Toolchain and reproduction

SAS Base, versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
sas hello.sas
```

## Expected result and status

Hello, World! in the SAS log.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Commitments: SAS runtime/licenza unavailable; hanging execution logs and parser.

## Primary sources

- https://support.sas.com/documentation/cdl/en/basess/58133/HTML/default/a002108635.htm

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.sas` | [hello.sas](hello.sas) created; verification pending |
