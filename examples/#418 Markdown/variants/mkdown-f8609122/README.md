# 0418: Markdown: `.mkdown`

## Latest recorded verification

**Syntax and behavior verified** for `.mkdown`. Unchanged suffix variant; main example status unchanged. [Recorded evidence](../../verification/native_20261104_followup_2e6d6b646f776e.json).

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#418 Markdown/hello.md.

Required toolchain: Python 3.13.9 + markdown-it-py 4.2.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.mkdown; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: HTML <h1> Hello, World! </h1> and LF; stdout greeting and LF.

Status before this check: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.mkdown`: `0b4fdcfa10c709d9ab7d679fed4eb63742b2f51d8b073ec9016e5c5165d148ae`
- `verify.py`: `303168592113315bafc46e5cf9edc793a9161e1ccafb5b901c2e87ff64f46b6b`

Primary sources:

- https://spec.commonmark.org/0.31.2/
- https://github.com/executablebooks/markdown-it-py
