# 0301: IDL: `.dlm`

Role: Descriptor IDL Dynamically Loadable Module: name, version and declaration of routine; not .pro. code

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: NV5 Geospatial IDL proprietario; versione da registrare. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
IDL con SDK: compilare una libreria che esporta IDL_Load e CORPUS_HELLO; impostare !DLM_PATH e DLM_LOAD, "corpus_hello"
```

Expected result: IDL records the module described; a future native press routine Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.
- The shared library and the owner SDK IDL are not available; the descriptor only does not implement the routine.

SHA-256 of variant files:

- `hello.dlm`: `e9f8b8157912ff4e4ebd03da09de88c3663d463d6cf61aad64bf48cd06ffd680`

Primary sources:

- https://www.nv5geospatialsoftware.com/docs/DLM.html
- https://www.nv5geospatialsoftware.com/docs/PRINT.html
- https://www.nv5geospatialsoftware.com/docs/Defining_Procedures.html
