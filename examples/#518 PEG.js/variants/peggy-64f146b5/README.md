# 0518: PEG.js: `.peggy`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#518 PEG.js / hello.pegjs.

Required toolchain: Node.js 22.20.0 + Peggy. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.peggy; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: recognized greeting, wrong input refused.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.peggy`: `3636735c9bbd19ff288579658e3b66fdab1bf82ecc3be189c7557b5217e60397`
- `verify.cjs`: `be801a915083bf6331a0cae3578224abb89d2c063801eb69f18c64ba0900f890`

Primary sources:

- https://peggyjs.org/documentation.html
