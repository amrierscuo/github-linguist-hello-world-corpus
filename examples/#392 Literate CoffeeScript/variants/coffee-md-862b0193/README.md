# 0392: Literate CoffeeScript: `.coffee.md`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#392 Literate CoffeeScript/hello.litcoffee.

Required toolchain: coffeescript 2.7.0; Node 22.20.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.coffee.md; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: Ignored test, compiled indented code; stdout Hello, World! plus newline.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.coffee.md`: `47a98ff081bd84d8e6256f4931fd20d4e684fa704b1042f6e75b25b01a62a084`
- `package.json`: `f4996b9974b12a80f0c6b5a867c49809c02a052f28a0b98bb1b68dc023e5bfeb`

Primary sources:

- https://coffeescript.org/#literate
- https://github.com/jashkenas/coffeescript
