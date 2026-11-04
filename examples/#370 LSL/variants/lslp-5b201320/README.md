# 0370: LSL: `.lslp`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#370 LSL/hello.lsl.

Required toolchain: Second Life/LSL o runtime compatibile; versione da registrare. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.lslp; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: Owner's Chat contains Hello, World!.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.lslp`: `28efa102dea0f125f0722c1d15b4b5ade5f749c167ec974684d96ba2193160e3`

Primary sources:

- https://wiki.secondlife.com/wiki/LSL_Portal
- https://wiki.secondlife.com/wiki/LlOwnerSay
