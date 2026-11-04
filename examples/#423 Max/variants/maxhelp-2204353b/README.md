# 0423: Max: `.maxhelp`

Role: Max Help Patch: same JSON patcher document from the main source; the message box remains connected to print.

Provenience: adaptation of the original corpus patcher; the message box content protects comma with backslash to send only one message.

Required toolchain: Cycling ’74 Max 8+. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.maxhelp; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: patch accepted; console greeting: Hello, World!.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.maxhelp`: `0891aa513d9e3cedeb7b8d09e835264e3e52aa063c028c4627230767117e8540`

Primary sources:

- https://docs.cycling74.com/reference/message/
- https://docs.cycling74.com/reference/print/

Source on the comma separator: https://docs.cycling74.com/reference/message/
