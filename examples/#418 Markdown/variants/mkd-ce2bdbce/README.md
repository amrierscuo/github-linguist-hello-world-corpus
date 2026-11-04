# 0418: Markdown: `.mkd`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#418 Markdown/hello.md.

Required toolchain: Python 3.13.9 + markdown-it-py 4.2.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.mkd; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: HTML <h1> Hello, World! </h1> and LF; stdout greeting and LF.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.mkd`: `0b4fdcfa10c709d9ab7d679fed4eb63742b2f51d8b073ec9016e5c5165d148ae`
- `verify.py`: `7e64f44dd33df835c7f4822abf841227dc067f361f55b9a705c6a32da3076ca1`

Primary sources:

- https://spec.commonmark.org/0.31.2/
- https://github.com/executablebooks/markdown-it-py
