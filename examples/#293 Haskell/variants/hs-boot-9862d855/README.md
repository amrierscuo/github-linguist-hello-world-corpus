# 0293: Haskell: `.hs-boot`

Role: hs-boot interface for a SOURCE cyclic dependence: only signature, not main.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Hugs98 September2006, pacchetto98.200609.21-6build3 e librerie bundled Ubuntu. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
GHC: ghc --make Main.hs -o hello; ./hello
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `Audience.hs`: `906024b298648c82869a886f69b07ea87c1ebf2758e5f4b09d8402c51e03f844`
- `Greeting.hs`: `2c58ca0bf12a93c2bbedcff45ee04d8b93053c62b892e439783a2a1e089911e6`
- `Greeting.hs-boot`: `97ddd611f6354573607be4994915078c05a5276e4ba88008a3f442ed9f5e3cd3`
- `Main.hs`: `6314a6128930c6a895d4bee637b87a00a0c45505b97531ea2f1dce7059342f15`

Primary sources:

- https://downloads.haskell.org/ghc/latest/docs/users_guide/separate_compilation.html#mutually-recursive-modules-and-hs-boot-files
- https://www.haskell.org/hugs/
- https://www.haskell.org/onlinereport/haskell2010/haskellch9.html
