# #476 Noir

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Fill Noir and return the public array ASCII which represents Hello, World!.

main returns13u8 as the public output of the circuit; Nargo.toml describes the local package. Greeting is given tipato of the circuit, not a comment or print foreign to the language.

## Toolchain and reproduction

Noir/nargo originale; versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
nargo check
```

```text
nargo execute
```

## Expected result and status

Array pubblico72,101,108,108,111,44,32,87,111,114,108,100,33.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Commitments: Compiler/runtime nargo not prepared.

## Primary sources

- https://github.com/noir-lang/noir
- https://noir-lang.org/docs/

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.nr` | [main.nr](src/main.nr) created; verification pending |
