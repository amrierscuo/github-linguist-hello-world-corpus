# 0537: Pike: `.pmod`

Ruolo: Modulo Pike con funzione greeting; driver usa compile_file.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Genuine Pike language interpreter, Pike v8.0 release 1738 Copyright © 1994-2022 Linköping University; Pike comes with ABSOLUTELY NO WARRANTY; This is free software and you are; welcome to redistribute it under certain conditions; read the files; COPYING and COPYRIGHT in the Pike distribution for more details.. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
pike driver.pike
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `driver.pike`: `36e426eddaf91634160a0161c42786112ad3fc9fe3a27e9a52e7136160d5558b`
- `hello.pmod`: `eed01d39064c3a993ca9964cd24697fea5decd5fff30016bf8e902f910dd28b8`

Primary sources:

- https://pike.lysator.liu.se/docs/tutorial/
- https://pike.lysator.liu.se/docs/man/
