# 0550: PowerBuilder: `.pbt`

Role: Target PowerBuilder: AppName and LibList, text descriptor that reports a library to be created in the work.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Appeon PowerBuilder originale; versione da registrare. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
PowerBuilder: creare corpus_hello.pbl nel work, importare corpus_hello.sra e aprire hello.pbt
```

Expected result: Target of test application showing Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.
- The .pbl bookcase requires original creation PowerBuilder; a fictitious track is not distributed.

SHA-256 of variant files:

- `corpus_hello.sra`: `d23ab37da300ef38690905e9198640b61f22f0402ed11965d556f548ab7a6c18`
- `hello.pbt`: `a4b149e6f77eba43aae01d751cebd8fc08235db285dc2e7134429ef390de9507`

Primary sources:

- https://docs.appeon.com/pb2019r3/pbug/ch02s01.html
- https://www.appeon.com/system/files/product-manual/powerscript_reference_v2021.pdf
