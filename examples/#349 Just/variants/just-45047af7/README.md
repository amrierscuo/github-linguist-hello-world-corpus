# 0349: Just: `.just`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#349 Just/justfile.

Required toolchain: Official Just recipe parser and runner, just 1.58.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.just; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: Listed recipe; exit 0; exact greeting.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.just`: `23a4dece0400d8027f0cf079b6e0f3473054c6ff51f667a53695e59bb0d2e941`

Primary sources:

- https://just.systems/man/en/
- https://github.com/casey/just
