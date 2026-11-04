# 0441: Module Management System: `.mmk`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#441 Module Management System/descrip.mms.

Required toolchain: Required genuine toolchain not available/configured, non disponibile / non verificata. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.mmk; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.mmk`: `4451655170d79a5b7d4705ca6f969d0e27892409526cdfe2835bd5157bf43f98`

Primary sources:

- https://docs.vmssoftware.com/docs/vsi-decset-for-openvms-guide-to-the-module-management-system.pdf
