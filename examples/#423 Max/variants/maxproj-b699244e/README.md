# 0423: Max: `.maxproj`

Role: Descriptor project Max authored textual with structure attested by a project published by his author: name greeting and local patcher. Dates fisse illustrative ( 2000-01-01 ); it does not declare export from a Max executed.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Cycling ’74 Max 8+. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Max originale: aprire hello.maxproj in directory di lavoro; confermare progetto e hello.maxpat locale top-level; eseguire patcher e leggere console.
```

Expected result: Hello, World! project with greeting patcher; schema/loading original pendants.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.
- Max unavailable: JSON is written according to a project structure attested but the application scheme and the project loading were not verified.

SHA-256 of variant files:

- `hello.maxpat`: `0891aa513d9e3cedeb7b8d09e835264e3e52aa063c028c4627230767117e8540`
- `hello.maxproj`: `613a5748c7b92e814d820b79bcdc68e28914abde73e883de3d26400bbdd3dc05`

Primary sources:

- https://docs.cycling74.com/userguide/projects/
- https://github.com/rennyhyde/HARD2500/blob/main/HARD_2500.maxproj
- https://docs.cycling74.com/reference/message/
- https://docs.cycling74.com/reference/print/
