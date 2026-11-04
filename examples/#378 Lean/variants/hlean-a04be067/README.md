# 0378: Lean: `.hlean`

Ruolo: Definizione Lean 2 HoTT di una stringa del saluto; eval riduce il termine. Non usa IO/main Lean 3.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Lean3.51.1 community ufficiale Windows. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Lean 2 originale con libreria HoTT sul LEAN_PATH: lean hello.hlean
```

Expected result: Elaboration of the term greeting:string and eval output with the Hello, World! string (the formatting of the pretty-printer can include quotes).

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.
- Lean 2 and compatible HoTT bookshelf not prepared. Lean 3 and Lean 4 do not validate this historic dialect.

SHA-256 of variant files:

- `hello.hlean`: `bd1f6961b5ef47fc720b2455279d2f8ba0c87eb479f12e3bfd0389549e9d0ba1`

Primary sources:

- https://raw.githubusercontent.com/leanprover/tutorial/master/05_Interacting_with_Lean.org
- https://raw.githubusercontent.com/leanprover/lean2/master/hott/init/datatypes.hlean
- https://github.com/leanprover/lean2
- https://github.com/leanprover-community/lean/releases/tag/v3.51.1
- https://leanprover-community.github.io/lean3/
