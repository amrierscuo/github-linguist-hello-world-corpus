# 0382: Lex: `.lex`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#382 Lex/hello.l.

Required toolchain: flex 2.6.4; GCC 13.3.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.lex; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: Scanner exit 0; a Hello, World! line.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.lex`: `4ab326b779b681bd4737c8cd30b9bd6cc36af946eb36e6d82fb0b138a904c067`
- `input.txt`: `5891b5b522d5df086d0ff0b110fbd9d21bb4fc7163af34d08286a2e846f6be03`

Primary sources:

- https://westes.github.io/flex/manual/
- https://westes.github.io/flex/manual/Simple-Examples.html
