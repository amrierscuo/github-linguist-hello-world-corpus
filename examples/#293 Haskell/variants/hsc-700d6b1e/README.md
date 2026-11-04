# 0293: Haskell: `.hsc`

Ruolo: Sorgente hsc2hs: preprocessamento include C, poi normale programma Haskell.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Hugs98 September2006, pacchetto98.200609.21-6build3 e librerie bundled Ubuntu. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
hsc2hs hello.hsc -o Main.hs; ghc Main.hs -o hello; ./hello
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.hsc`: `06ea4d8ec1cf1da2f3deade5a82f24cdffd8d7d095cc8180e805159e0d865e8c`

Primary sources:

- https://downloads.haskell.org/ghc/latest/docs/users_guide/utils.html#hsc2hs
- https://www.haskell.org/hugs/
- https://www.haskell.org/onlinereport/haskell2010/haskellch9.html
