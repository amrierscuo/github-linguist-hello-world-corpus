# 0503: OpenEdge ABL: `.cls`

Role: ABL class with static Greeting method, distinct from the .p. procedure

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Progress OpenEdge ABL. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
OpenEdge: compilare CorpusGreeting.cls e driver.p; eseguire driver in sessione di test
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `CorpusGreeting.cls`: `3aef1f12e6194253b8816630a77925b91adb49c0dd217b549995866241085261`
- `driver.p`: `50db11866901900381077e0c98deb980df85de30cfdc2f8c0e9be7b9db3ec34c`

Primary sources:

- https://docs.progress.com/bundle/abl-reference/page/CLASS-statement.html
- https://docs.progress.com/bundle/abl-reference/page/MESSAGE-statement.html
