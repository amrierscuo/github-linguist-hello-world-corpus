# 0283: HTML+ERB: `.rhtml`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#283 HTML+ERB/hello.erb.

Required toolchain: Ruby3.2.3, ERB della libreria standard. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.rhtml; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: stdout <p> Hello, World! </p> followed by newline; exit 0.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.rhtml`: `be111e0cf6656631175533dad2c49ae5667c01ea09c2589089e5f7247bb6c962`
- `render.rb`: `0ded8de25e33e448a6ceeb16159f7dffb20ed85079ff9b8c526b0bfbdec566c7`

Primary sources:

- https://docs.ruby-lang.org/en/3.2/ERB.html
