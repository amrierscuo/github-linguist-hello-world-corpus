# 0384: LilyPond: `.ily`

Role: Includes LilyPond with greeting markup; separate driver includes it.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: LilyPond 2.24 compatibile; versione effettiva da registrare. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
lilypond driver.ly
```

Expected result: Text Hello, World! in rendering PDF/SVG

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `driver.ly`: `9b7b92a752134d5e08f55976a8ebab2b85d7331992984095ec8dbe9eba02f34f`
- `hello.ily`: `81e9dd825021b2137b18e7e0029c998a4f8041054f24e852ea16ff2964d4de24`

Primary sources:

- https://lilypond.org/doc/v2.24/Documentation/notation/including-lilypond-files
- https://lilypond.org/doc/v2.24/Documentation/learning/
- https://lilypond.org/doc/v2.24/Documentation/usage/command_002dline-usage
