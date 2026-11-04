# 0550: PowerBuilder: `.srw`

Role: Subject window PowerBuilder exportable with title of greeting and open MessageBox.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Appeon PowerBuilder originale; versione da registrare. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
PowerBuilder: importare w_hello.srw in libreria di test e Open(w_hello) da application
```

Expected result: Title and MessageBox Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `w_hello.srw`: `c31fd44de127e585c896a184ad44ed286f3b1827c91c488f6e38e401d8ad3722`

Primary sources:

- https://docs.appeon.com/pb2019r3/pbug/ch02s01.html
- https://www.appeon.com/system/files/product-manual/powerscript_reference_v2021.pdf
