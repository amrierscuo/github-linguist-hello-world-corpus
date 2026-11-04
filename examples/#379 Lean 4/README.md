# #379 Lean 4

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Check the greeting_length theorem in Lean4 and print Hello, World!.

Use String, IO Unit and the tactic decides of Lean4. The distribuzione4.0.0 is held separate from the compiler3.51.1; the theorem and main are verified by the respective original environment.

## Toolchain and reproduction

Lean4.0.0 ufficiale Linux

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

- https://lean-lang.org/documentation/
- https://github.com/leanprover/lean4/releases/tag/v4.0.0

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.lean` | [hello.lean](hello.lean) verified |
