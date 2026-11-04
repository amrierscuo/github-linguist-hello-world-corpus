# #545 Pony

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Fill out Pony and print Hello, World!.

The actor Main receives Env, creates audiences and writes with env.out.print.

## Toolchain and reproduction

ponyc originale; versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
ponyc .
```

```text
./main
```

## Expected result and status

Hello, World! seguito da newline; exit0.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Commitments: Compiler/runtime Pony not prepared.

## Primary sources

- https://tutorial.ponylang.io/getting-started/hello-world.html
- https://tutorial.ponylang.io/expressions/variables.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pony` | [main.pony](main.pony) created; verification pending |
