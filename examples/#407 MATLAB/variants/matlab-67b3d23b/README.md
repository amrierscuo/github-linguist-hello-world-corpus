# 0407: MATLAB: `.matlab`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#407 MATLAB/hello.m.

Required toolchain: MATLAB oppure GNU Octave per questo sottoinsieme compatibile. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.matlab; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: stdout Hello, World! and LF.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.matlab`: `a7c821fc75515533494fb9259e141f9a8206c7aeb15bccdc251747f60d440b60`

Primary sources:

- https://www.mathworks.com/help/matlab/ref/disp.html
- https://docs.octave.org/latest/
