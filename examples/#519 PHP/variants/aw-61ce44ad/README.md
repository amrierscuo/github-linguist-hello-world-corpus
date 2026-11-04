# 0519: PHP: `.aw`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#519 PHP/hello.php.

Required toolchain: PHP 8.3.6 native Ubuntu CLI. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.aw; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: stdout Hello, World! and newline.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.aw`: `e93e2a16546a0c99a77c7bd39811a3b248dfd9253bf3620cb4b55abe252ccfab`

Primary sources:

- https://www.php.net/manual/en/function.echo.php
