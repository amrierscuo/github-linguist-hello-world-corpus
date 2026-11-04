# 0398: Logtalk: `.logtalk`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#398 Logtalk/hello.lgt.

Required toolchain: Logtalk 3.102.0 original lgt31020stable; SWI-Prolog version 9.0.4 for x86_64-linux. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.logtalk; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: Oggetto/public preached compiled; message send emette Hello, World! more newline, exit 0.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.logtalk`: `c773f66269f7f241a6271a1c3574ace6668fb76844ecaa0996ad38cb010578ad`

Primary sources:

- https://logtalk.org/learning.html
- https://logtalk.org/documentation.html
- https://github.com/LogtalkDotOrg/logtalk3/tree/lgt31020stable
