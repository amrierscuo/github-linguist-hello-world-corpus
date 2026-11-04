# 0314: Inno Setup: `.isl`

Role: Inno Setup messages file: WelcomeLabel1 localized override.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Inno Setup ISCC; versione da registrare. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
ISCC driver.iss; avviare l’installer solo in ambiente di test per leggere WelcomeLabel1
```

Expected result: The initial wizard message contains Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `driver.iss`: `27b0d587ceff68c99ddd4f95c40a3558eb94b63c82a00b098b9cff0ce483b7e7`
- `hello.isl`: `f7eed62fa011bddb6269cbbb42e0bfef5ddffedf20ae83d734d303a7207be7be`

Primary sources:

- https://jrsoftware.org/ishelp/topic_messagessection.htm
- https://jrsoftware.org/ishelp/topic_setupsection.htm
- https://jrsoftware.org/ishelp/topic_scriptevents.htm
- https://jrsoftware.org/ishelp/topic_isxfunc_msgbox.htm
