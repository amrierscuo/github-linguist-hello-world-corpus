# #549 Power Query

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Evaluate an expression PowerQuery M and get Hello, World!.

le alloy Audience and Greeting; & concatena stringhe and in return the value. The program is M, distinguished by PowerShell.

## Toolchain and reproduction

PowerQuery M engine originale; versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
Caricare hello.pq in una query vuota PowerQuery e valutare.
```

## Expected result and status

Result string Hello, World!.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Commitments: Engine PowerQuery not prepared; parsing/evaluation pendants.

## Primary sources

- https://learn.microsoft.com/en-us/powerquery-m/m-spec-introduction
- https://learn.microsoft.com/en-us/powerquery-m/m-spec-consolidated-grammar

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pq` | [hello.pq](hello.pq) created; verification pending |
