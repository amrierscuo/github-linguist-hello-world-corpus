# 0530: Pawn: `.inc`

Role: Header Pawn with stock function not to impose main in the included file.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Required genuine compiler/runtime, non disponibile / non verificata. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
pawncc driver.pwn; runtime AMX con binding console originale
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `driver.pwn`: `f20e4f1d693a36f6c37493b85b0c67c7a4e4f7add5ede167262d0518cc7efb4b`
- `hello.inc`: `c24e2ab2a428839585147ac9efb96dbfdf5dc76d6dfa755cc1d6c040653cd54f`

Primary sources:

- https://github.com/compuphase/pawn
- https://compuphase.com/pawn/pawn.htm
