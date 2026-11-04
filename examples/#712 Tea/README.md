# #712 Tea

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Rendering a Tea template with audience = World parameter.

Tea Template in the Java TeaTrove system: the text region and the audience expression produce greetings.

## Toolchain and reproduction

Tea compiler/runtime TeaTrove, versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
TeaTrove: compilare hello.tea e invocare hello con parametro World
```

## Expected result and status

Hello, World! con newline finale.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Commitments: TeaTrove compiler/runtime not available; parser and pendent rendering.

## Primary sources

- https://github.com/teatrove/teatrove/wiki/Tea-Templates

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.tea` | [hello.tea](hello.tea) created; verification pending |
