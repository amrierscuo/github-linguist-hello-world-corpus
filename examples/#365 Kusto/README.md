# #365 Kusto

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Analyze Kusto and return, with the query engine, the greeting column containing Hello, World!.

The driver loads the original Microsoft assembly, uses ParseAndAnalyze and compares diagnostics. print and strcat are operatori/funzioni Kusto; the parser verification does not query the service.

## Toolchain and reproduction

Microsoft.Azure.Kusto.Language12.4.1; PowerShell7 for the driver; query engine not prepared

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
pwsh -NoProfile -File verify.ps1 /path/to/Kusto.Language.dll
```

## Expected result and status

Parser and analyzer produce zero diagnostics; expected engine: a greeting line= Hello, World!.

Artifact created: yes. syntax verified: yes. behavior verified: no.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

Commitments: Motor Kusto unavailable; execution of the pending query.

## Primary sources

- https://learn.microsoft.com/en-us/kusto/query/print-operator
- https://learn.microsoft.com/en-us/kusto/query/strcat-function
- https://github.com/microsoft/Kusto-Query-Language

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.csl` | [hello.csl](variants/csl-341667e5/hello.csl) created; verification pending |
| `.kql` | [hello.kql](hello.kql) syntax verified |
