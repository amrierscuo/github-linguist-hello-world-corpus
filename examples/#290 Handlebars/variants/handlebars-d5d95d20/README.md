# 0290: Handlebars: `.handlebars`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#290 Handlebars/hello.hbs.

Required toolchain: Handlebars4.7.8, Node.js22.20.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.handlebars; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: stdout <p> Hello, World! </p> followed by newline; exit 0.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.handlebars`: `c8a5cdec3b03ec742a9a6f1062f1ca729d8d0883a2fcf37c5758b5fb743d4c2c`
- `render.js`: `a9b1ebd90c02522e9c4f49bab5cb016aaa1f8c2c4779586e6932e5bdb7852fdf`

Primary sources:

- https://handlebarsjs.com/guide/
