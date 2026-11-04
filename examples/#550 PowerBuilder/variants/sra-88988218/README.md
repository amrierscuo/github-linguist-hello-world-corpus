# 0550: PowerBuilder: `.sra`

Role: Subject application PowerBuilder exportable, open event shows greeting.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Appeon PowerBuilder originale; versione da registrare. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
PowerBuilder: importare corpus_hello.sra in libreria di test e impostare application target
```

Expected result: MessageBox Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `corpus_hello.sra`: `d23ab37da300ef38690905e9198640b61f22f0402ed11965d556f548ab7a6c18`

Primary sources:

- https://docs.appeon.com/pb2019r3/pbug/ch02s01.html
- https://www.appeon.com/system/files/product-manual/powerscript_reference_v2021.pdf
