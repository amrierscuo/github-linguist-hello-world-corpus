# 0547: PostCSS: `.postcss`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#547 PostCSS/hello.pcss.

Required toolchain: PostCSS8 e postcss-custom-properties originali; versioni effettive nel log. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.postcss; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: CSS transformer contains content: "Hello, World!".

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.postcss`: `7da058442245be1726962a0b9b571bf6e9e0f97b017d63380e9787759d71779c`
- `verify.js`: `ed71830e46f5dddcdd00a451ccff75fb5d0de3ca21641cf162a74c339d01a2db`

Primary sources:

- https://postcss.org/
- https://github.com/csstools/postcss-plugins/tree/main/plugins/postcss-custom-properties
