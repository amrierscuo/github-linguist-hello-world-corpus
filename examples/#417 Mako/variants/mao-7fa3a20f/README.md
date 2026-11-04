# 0417: Mako: `.mao`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#417 Mako/hello.mako.

Required toolchain: Python 3.13.9 + Mako 1.4.3. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.mao; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: stdout Hello, World! and LF, exit 0.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.mao`: `add1ff9a5370e224b33c18df89e709f00ed56d5c1cac0e0a895f9e85555b63d0`
- `verify.py`: `816bad55b8f7d799691457565d7fe3e4559528a2b1f3464f273de81eadfc3879`

Primary sources:

- https://docs.makotemplates.org/en/latest/syntax.html
