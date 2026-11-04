# 0437: Mirah: `.druby`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#437 Mirah/hello.mirah.

Required toolchain: Mirah compiler e JVM compatibili. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.druby; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: stdout Hello, World! and newline.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.druby`: `ba07db485f6c6435a90f606a9a265d92857a1ce6fb411b80a82977938b737d52`

Primary sources:

- https://github.com/mirah/mirah
