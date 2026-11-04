# 0558: Prolog: `.plt`

Role: Unit test Prolog plunit with verification of greeting, distinct from main.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: SWI-Prolog9.0.4 ufficiale Ubuntu. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
swipl -q -g run_tests -t halt hello.plt
```

Expected result: Test plunit PASS

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.plt`: `7dfb71c8bc69e695d125e6ae16a614c01807dcddb1a0c7062fb5679a41d5a7f1`

Primary sources:

- https://www.swi-prolog.org/pldoc/doc_for?object=section(%27packages/plunit.html%27)
- https://www.swi-prolog.org/pldoc/doc_for?object=atomic_list_concat/2
- https://www.swi-prolog.org/pldoc/doc_for?object=initialization/2
