# 0423: Max: `.mxt`

Role: Patcher Max legacy textual max v2/#N/#P, with list of 13 codes ASCII greeting codes -> itoa -> print. It is not the maxb binary format; the numerical message does not use comma separators.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Cycling ’74 Max 8+. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Max originale compatibile: aprire hello.mxt come patcher testuale (o importare dal clipboard) e leggere la console; verificare il reader legacy e il collegamento loadbang/message/itoa/print.
```

Expected result: Console with Hello, World! symbol (prefix print corpus allowed).

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.
- Reader Max legacy not executed; express greeting as ASCII codes and converted from itoa, avoiding ambiguity of the serialization of the subparagraph.

SHA-256 of variant files:

- `hello.mxt`: `9f2eb2ebe46c91b32617235c1be7329ec11fce04663c86b9ee979bfad7c9f26f`

Primary sources:

- https://docs.cycling74.com/userguide/filetypes/
- https://docs.cycling74.com/reference/itoa/
- https://github.com/github-linguist/linguist/blob/main/samples/Max/Hello.mxt
- https://docs.cycling74.com/reference/message/
- https://docs.cycling74.com/reference/print/
