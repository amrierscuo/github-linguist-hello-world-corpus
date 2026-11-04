# 0323: JFlex: `.flex`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#323 JFlex/hello.jflex.

Required toolchain: JFlex 1.9.1 + CUP runtime 11b-20160615-3 + OpenJDK 21.0.12. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.flex; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: 0 output; stdout Hello, World! followed by newline.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.flex`: `7038d4ba02a30781506a19f385ae8b2ea69fc9aa5183d8e50fc681dee81a0edf`
- `input.txt`: `aa1db5c660d3d1f3f4f9361b9848694300929be94b74c84452a87420c59e5df9`

Primary sources:

- https://jflex.de/manual.html
