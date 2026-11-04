# #378 Lean

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Check the type and length of greeting in Lean3, then print Hello, World!.

Import system.io, use string and i API unit Lean3. The rfl test and the program are processed by the original Lean3 compiler/kernel before execution.

## Toolchain and reproduction

Lean3.51.1 community ufficiale Windows

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
lean hello.lean
```

```text
lean --run hello.lean
```

## Expected result and status

The kernel accepts greeting.length = 13; stdout Hello, World! followed by newline.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://github.com/leanprover-community/lean/releases/tag/v3.51.1
- https://leanprover-community.github.io/lean3/

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.lean` | [hello.lean](hello.lean) verified |
| `.hlean` | [hello.hlean](variants/hlean-a04be067/hello.hlean) created; verification pending |
