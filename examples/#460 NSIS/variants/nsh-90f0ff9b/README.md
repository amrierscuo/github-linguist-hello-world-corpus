# 0460: NSIS: `.nsh`

Ruolo: Header NSIS con macro di messaggio, include guard e script driver.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Official NSIS script compiler and native Windows installer generator, v3.09-4. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
makensis driver.nsi; eseguire solo installer di test e leggere dettagli
```

Expected result: Hello, World! in details

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `driver.nsi`: `8ef590162df9e0ccb9ea1aca74bd3ab27f6ac49ce0b9d192fc394b34dcfea864`
- `hello.nsh`: `f728ae2ec188854dd45cc317be82c9a72d33a4903bd8a5bea99e0dee916d24b5`

Primary sources:

- https://nsis.sourceforge.io/Docs/Chapter5.html
- https://nsis.sourceforge.io/Docs/Chapter4.html
- https://nsis.sourceforge.io/Docs/
