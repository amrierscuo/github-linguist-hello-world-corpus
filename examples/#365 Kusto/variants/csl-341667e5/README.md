# 0365: Kusto: `.csl`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#365 Kusto/hello.kql.

Required toolchain: Microsoft.Azure.Kusto.Language12.4.1; PowerShell7 per il driver; query engine non preparato. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.csl; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: Parser and analyzer produce zero diagnostics; expected engine: a greeting line= Hello, World!.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.csl`: `70a3f13183759f7b0b96a2d2ef87da52e07baa0cfadc89a08880c41a92a66b01`
- `verify.ps1`: `2541d629bb8ade880fe6eab58368c231f742a024c7f4fa55df1d26b0503f4a31`

Primary sources:

- https://learn.microsoft.com/en-us/kusto/query/print-operator
- https://learn.microsoft.com/en-us/kusto/query/strcat-function
- https://github.com/microsoft/Kusto-Query-Language
